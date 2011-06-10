%define		module	memcached
Summary:	memcached python client
Summary(pl.UTF-8):	Pythonowy klient memcached
Name:		python-%{module}
Version:	1.47
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	ftp://ftp.tummy.com/pub/python-%{module}/%{name}-%{version}.tar.gz
# Source0-md5:	e4e9d65e5721a1bb01f8d657ddf3f03e
URL:		http://www.danga.com/memcached/apis.bml
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.174
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
memcached python client.

%description -l pl.UTF-8
Pythonowy klient memcached.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root $RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/*.py[co]
%{py_sitescriptdir}/python_memcached-*.egg-info
