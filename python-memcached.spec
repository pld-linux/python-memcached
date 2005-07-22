%define		module	memcached
Summary:	memcached python client
Name:		python-%{module}
Version:	1.2
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	http://www.danga.com/memcached/dist/python-%{module}-%{version}.tar.gz
# Source0-md5:	7bbba370429bd3d7ab70bbf0828d841c
URL:		http://www.danga.com/memcached/apis.bml
BuildRequires:	rpmbuild(macros) >= 1.174
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
memcached python client.

%prep
%setup -q -n python-%{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{py_scriptdir}/site-packages/*.py[co]
