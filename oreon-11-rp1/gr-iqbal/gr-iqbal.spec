%global source0_hash de9dcd2ae2172596dc0752cf554d7edb5b6cb67d44f49c77feff287bff1d3541
%global git_commit fbee239a6fb36dd2fb564f6e6a0d393c4bc844db
%global git_date 20210210
%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}
Name:          gr-iqbal
URL:           https://github.com/osmocom/gr-iqbal
Version:       0.38.2
Release:        1%{?dist}
License:       GPL-3.0-or-later
Summary:        GNURadio block for suppressing IQ imbalance
Source0:        https://github.com/osmocom/%{name}/archive/%{git_commit}/%{name}-%{git_commit}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fftw-devel
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  gnuradio-devel
BuildRequires:  graphviz
BuildRequires:  libosmo-dsp-devel
BuildRequires:  libunwind-devel
BuildRequires:  pybind11-devel
BuildRequires:  python3-devel
BuildRequires:  spdlog-devel
# /oreon:deps
%description
This GNURadio block can suppress IQ imbalance in the RX path of
quadrature receivers.

%package devel
Summary:          Development files for gr-iqbal
Requires:         %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for gr-iqbal.

%package doc
Summary:          Documentation files for gr-iqbal
Requires:         %{name} = %{version}-%{release}
%description doc
Documentation files for gr-iqbal.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{git_commit}

%build

%cmake -DENABLE_DOXYGEN=on -DGR_PKG_DOC_DIR=%{_docdir}/%{name}
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{_docdir}
mv %{buildroot}%{_datadir}/doc/gr-iqbalance %{buildroot}%{_docdir}/%{name}
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gr-iqbal-devel -f %{oreon_filedir}/gr-iqbal-devel.list
%files -n gr-iqbal-doc -f %{oreon_filedir}/gr-iqbal-doc.list

%changelog

%autochangelog
