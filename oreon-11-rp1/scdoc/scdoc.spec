%global source0_hash 98780bbdf16c1bce89ef3a8c0f537ac6e4ea77087b609e7698857614488a2a62
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: scdoc
Version: 1.11.5
Release: 1%{?dist}
Summary: Tool for generating roff manual pages
License: MIT
URL: https://git.sr.ht/~sircmpwn/scdoc
Source0: https://git.sr.ht/~sircmpwn/scdoc/archive/%{version}.tar.gz#/scdoc-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make

%description
scdoc is a simple man page generator written for POSIX systems in C99.

%prep
%oreon_sha256
%autosetup -n scdoc-%{version} -p1

%build
%oreon_make PREFIX=%{_prefix} PCDIR=%{_datadir}/pkgconfig LDFLAGS="%{build_ldflags}" CFLAGS="%{build_cflags}"

%install
%oreon_make_install PREFIX=%{_prefix} PCDIR=%{_datadir}/pkgconfig

%files
%license COPYING
%{_bindir}/scdoc
%{_mandir}/man1/scdoc.1*
%{_mandir}/man5/scdoc.5*
%{_datadir}/pkgconfig/scdoc.pc
