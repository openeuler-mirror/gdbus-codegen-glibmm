%global debug_package %{nil}
Name:           gdbus-codegen-glibmm
Version:        1.0.0
Release:        2%{?dist}
Summary:        This is a cpp code generator for generating D-Bus stubs and proxies from XML introspection files.

License:        LGPL-2.1
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-jinja2

%description
This is a cpp code generator for generating D-Bus stubs and proxies from XML introspection files.


%prep
%autosetup -p1


%build
%{py3_build}

%install
rm -rf $RPM_BUILD_ROOT
%{py3_install}


%files
%{_bindir}/gdbus-codegen-glibmm3
%dir %{python3_sitelib}/codegen_glibmm
%dir %{python3_sitelib}/gdbus_codegen.glibmm-2.99.0-py3.7.egg-info
%{python3_sitelib}/codegen_glibmm/*
%{python3_sitelib}/gdbus_codegen.glibmm-2.99.0-py3.7.egg-info/*

%changelog
* Mon Aug 16 2021 xinminst <xuzhiling19991120@163.com> - 1.0.0-2.ky3
- adapt to riscv64

* Thu Apr  1 2021 tangjie02 <tangjie02@kylinos.com.cn> - 1.0.0-1.ky3
- New upstream source 1.0
- 
