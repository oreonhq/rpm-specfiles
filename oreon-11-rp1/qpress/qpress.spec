%global source0_hash cf06f7e750568a74453936203c34e8d29bd7778ee553960934bc36c3d7e2fcdb
%global forgeurl https://github.com/PierreLvx/qpress
Name:           qpress
Version:        20260802
Release:        1%{?dist}
Summary:        A portable file archiver using QuickLZ
License:        GPL-1.0-only and GPL-2.0-only and GPL-3.0-only
URL:            https://www.quicklz.com
Source0:        %{forgeurl}/archive/%{version}/%{name}-%{version}.tar.gz
Patch1:         https://github.com/PierreLvx/qpress/pull/8.patch
Patch2:         https://github.com/PierreLvx/qpress/pull/9.patch
Provides:       bundled(quicklz) = 1.4.1
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description
qpress is a portable file archiver using QuickLZ and designed to utilize fast
storage systems to their max. It's often faster than file copy because the
destination is smaller than the source.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%set_build_flags
export CXXFLAGS="$CXXFLAGS -Wno-alloc-size-larger-than"
%make_build
%install
%make_install PREFIX="%{_prefix}"
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
