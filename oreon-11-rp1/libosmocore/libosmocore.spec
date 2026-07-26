%global source0_hash 3daa1bdd4cb48628f2d137af6643203030199c48cbc88ec1e862a6830a047769

%global git_commit 84dcf73625513af44e711b2c99e21ee2c33b7eff
%global git_date 20250331

%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}

# export name=%%{name}
# export version=%%{version}
# export git_commit=%%{git_commit}
# export git_suffix=%%{git_suffix}
# git clone git://git.osmocom.org/libosmocore.git
# cd ${name}
# git archive --format=tar --prefix=${name}-${version}/ ${git_commit} | \
# bzip2 > ../${name}-${version}-${git_suffix}.tar.bz2

Name:             libosmocore
URL:              https://osmocom.org/projects/libosmocore
Version:          0.9.6
Release:          27.%{git_suffix}%{?dist}
# Automatically converted from old format: GPLv2+ and GPLv3+ and AGPLv3+ - review is highly recommended.
License:          GPL-2.0-or-later AND GPL-3.0-or-later AND AGPL-3.0-or-later
BuildRequires:    autoconf
BuildRequires:    automake
BuildRequires:    libtool
BuildRequires:    pcsc-lite-devel
BuildRequires:    doxygen
BuildRequires:    libtalloc-devel
BuildRequires:    liburing-devel
BuildRequires:    libusb1-devel
BuildRequires:    libmnl-devel
BuildRequires:    lksctp-tools-devel
BuildRequires:    gnutls-devel
BuildRequires:    findutils
BuildRequires:    sed
BuildRequires:    python3
BuildRequires:    make
Summary:          Utility functions for OsmocomBB, OpenBSC and related projects
Source0:          %{name}-%{version}-%{git_suffix}.tar.bz2

%description
A collection of common code used in various sub-projects inside the Osmocom
family of projects (OsmocomBB, OpenBSC, ...).

%package devel
Summary:          Development files for libosmocore
Requires:         %{name}%{?_isa} = %{version}-%{release}
# for /usr/include/osmocom directory
Requires:         libosmo-dsp-devel, libtalloc-devel

%description devel
Development files for libosmocore.

%package doc
Summary:        Documentation files for libosmocore
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
Documentation files for libosmocore.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
autoreconf -fi
%configure
%make_build

%install
%make_install
# Remove libtool archives
find %{buildroot} -name '*.la' -exec rm -f {} \;

%check
# reported upstream
%ifnarch s390x
make check
%endif

%files
%doc %{_docdir}/%{name}
# fallback for cases where there is no _licensdir
%exclude %{_docdir}/%{name}/codec
%exclude %{_docdir}/%{name}/core
%exclude %{_docdir}/%{name}/gsm
%exclude %{_docdir}/%{name}/vty
%{!?_licensedir:%global license %%doc}
%license COPYING
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%{_includedir}/osmocom/*
%{_includedir}/osmo-release.mk
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/osmo_*.m4

%files doc
%doc %{_docdir}/%{name}/codec
%doc %{_docdir}/%{name}/core
%doc %{_docdir}/%{name}/gsm
%doc %{_docdir}/%{name}/vty

%changelog
%autochangelog
