%define		module	memcached
Summary:	memcached python client
Summary(pl.UTF-8):   Pythonowy klient memcached
Name:		python-%{module}
Version:	1.2
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	http://www.danga.com/memcached/dist/python-%{module}-%{version}.tar.gz
# Source0-md5:	7bbba370429bd3d7ab70bbf0828d841c
URL:		http://www.danga.com/memcached/apis.bml
BuildRequires:	python
BuildRequires:	rpmbuild(macros) >= 1.174
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
memcached python client.

%description -l pl.UTF-8
Pythonowy klient memcached.

%prep
%setup -q -n python-%{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--root $RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/*.py[co]
