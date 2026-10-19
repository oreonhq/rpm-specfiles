%global source0_hash af86485a0c048e0414e9f469993403906c4ff8d8f6f26afd4ce0bfee6239fb59
%global git_commit f3646d04c138dc3279528808dcf6f847887e4a4f
%global git_date 20220804
%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}
Name:           gr-rds
Version:        3.10
Release:        1%{?dist}
Summary:        GNU Radio FM RDS Receiver
License:        GPL-3.0-or-later
URL:            https://github.com/bastibl/gr-rds
Source0:        https://github.com/bastibl/%{name}/archive/%{git_commit}/%{name}-%{git_date}git%{git_short_commit}.tar.gz
Requires:       gr-osmosdr
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  gnuradio-devel
BuildRequires:  libunwind-devel
BuildRequires:  pybind11-devel
BuildRequires:  python3-devel
BuildRequires:  spdlog-devel
# /oreon:deps
%description
%{summary}.

%package devel
Summary:          Development files for gr-rds
Requires:         %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%package doc
Summary:        Documentation files for gr-rds
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description doc
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{git_commit}

%build

%cmake -DENABLE_DOXYGEN=off -DGR_PKG_DOC_DIR=%{_docdir}/%{name}
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{_docdir}/%{name}/examples
install -p -m 644 examples/* %{buildroot}%{_docdir}/%{name}/examples
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gr-rds-devel -f %{oreon_filedir}/gr-rds-devel.list
%files -n gr-rds-doc -f %{oreon_filedir}/gr-rds-doc.list

%changelog

%autochangelog
