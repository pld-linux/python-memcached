%define		module	memcached
Summary:	memcached python client
Summary(pl.UTF-8):	Pythonowy klient memcached
Name:		python-%{module}
Version:	1.48
Release:	2
License:	GPL
Group:		Libraries/Python
Source0:	ftp://ftp.tummy.com/pub/python-%{module}/%{name}-%{version}.tar.gz
# Source0-md5:	58f8c328304df6aca1f8b60170e98932
URL:		http://www.tummy.com/Community/software/python-memcached/
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.174
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
memcached python client.

%description -l pl.UTF-8
Pythonowy klient memcached.

%prep
%setup -q

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install \
	--root $RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/*.py[co]
%{py_sitescriptdir}/python_memcached-*.egg-info
