%global source0_hash c642ae9b75fee120b2d96c712538bd2cf283228d2337df2cf2988e3c02678ef4
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: libyaml
Version: 0.2.5
Release: 1%{?dist}
Summary: YAML parser and emitter library
License: MIT
URL: https://github.com/yaml/libyaml
Source0: https://github.com/yaml/libyaml/releases/download/%{version}/yaml-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
%endif

%description
libyaml is a YAML 1.1 parser and emitter written in C.

%package devel
Summary: YAML parser and emitter library
Requires: libyaml%{?_isa} = %{version}-%{release}
Provides: pkgconfig(yaml-0.1)

%description devel
libyaml is a YAML 1.1 parser and emitter written in C.

%prep
%oreon_sha256
%autosetup -n yaml-%{version} -p1

%build
%oreon_configure --disable-static
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.la

%files
%license License
%{_libdir}/libyaml-0.so.2
%{_libdir}/libyaml-0.so.2.*

%files devel
%{_includedir}/yaml.h
%{_libdir}/libyaml-0.so
%{_libdir}/pkgconfig/yaml-0.1.pc
