%global source0_hash db10030528f3365c03755969619dd6789147d34fc588db8107364351085aebad
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: dwz
Version: 0.17
Release: 1%{?dist}
Summary: DWARF optimization and duplicate removal tool
License: GPL-3.0-or-later AND (GPL-3.0-or-later WITH GCC-exception-3.1) AND GPL-2.0-or-later AND (GPL-2.0-or-later WITH GCC-exception-2.0) AND LGPL-2.0-or-later
URL: https://sourceware.org/dwz/
Source0: https://sourceware.org/ftp/dwz/releases/dwz-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: make
BuildRequires: elfutils-libelf-devel
BuildRequires: xxhash-devel
%endif

%description
dwz optimizes DWARF debugging information and merges duplicate sections.

%prep
%oreon_sha256
%autosetup -n dwz -p1

%build
%oreon_make prefix=%{_prefix} mandir=%{_mandir} bindir=%{_bindir}

%install
%oreon_make_install prefix=%{_prefix} mandir=%{_mandir} bindir=%{_bindir}
%oreon_filelist

%files -f %{_builddir}/%{name}.files
%license COPYING COPYING3 COPYING.RUNTIME
