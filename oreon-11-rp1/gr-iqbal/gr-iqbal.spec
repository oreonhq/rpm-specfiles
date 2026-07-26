%global source0_hash de9dcd2ae2172596dc0752cf554d7edb5b6cb67d44f49c77feff287bff1d3541

%global git_commit fbee239a6fb36dd2fb564f6e6a0d393c4bc844db
%global git_date 20210210

%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}

Name:          gr-iqbal
#URL:           http://cgit.osmocom.org/gr-iqbal/
URL:           https://github.com/osmocom/gr-iqbal
Version:       0.38.2
Release:       42.%{git_suffix}%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:       GPL-3.0-or-later
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: gnuradio-devel
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: fftw-devel
BuildRequires: libosmo-dsp-devel
BuildRequires: python3-devel
# gnuradio dependency
BuildRequires: spdlog-devel
BuildRequires: gmp-devel
BuildRequires: libunwind-devel
BuildRequires: pybind11-devel
Summary:       GNURadio block for suppressing IQ imbalance
#Source0:       https://github.com/osmocom/gr-iqbal/archive/v%%{version}/%%{name}-%%{version}.tar.gz
Source0:       https://github.com/osmocom/gr-iqbal/archive/%{git_commit}/%{name}-%{git_commit}.tar.gz

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
# Doxygen bug
#BuildArch:        noarch

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

# Fix docs location
mkdir -p %{buildroot}%{_docdir}
mv %{buildroot}%{_datadir}/doc/gr-iqbalance %{buildroot}%{_docdir}/%{name}

%ldconfig_scriptlets

%files
%exclude %{_docdir}/%{name}/html
%exclude %{_docdir}/%{name}/xml
%doc COPYING AUTHORS
%{_libdir}/*.so.*
%{python3_sitearch}/*
%{_datadir}/gnuradio/grc/blocks/*

%files devel
%{_includedir}/gnuradio/iqbalance
%{_libdir}/*.so
%{_libdir}/cmake/gnuradio/*.cmake

%files doc
%doc %{_docdir}/%{name}/html
%doc %{_docdir}/%{name}/xml

%changelog
%autochangelog
