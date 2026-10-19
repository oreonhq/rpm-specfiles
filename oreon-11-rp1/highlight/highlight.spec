%global source0_hash 11c01ec5965ae9b0319bd7cb1a04ffd85ad8586176033a1fbe9a82f08e99ed56
Name:           highlight
Summary:        Universal source code to formatted text converter
Version:        4.19
Release:        1%{?dist}
License:        GPL-3.0-only
URL:            http://www.andre-simon.de/
Source0:        http://www.andre-simon.de/zip/%{name}-%{version}.tar.bz2
%bcond qt %[%{undefined rhel} || 0%{?rhel} < 10]
%if %{with qt}
%endif
%{?filter_setup:
%filter_from_provides /^perl(/d;
%filter_from_requires /^perl(/d;
%filter_from_requires /^\/bin\/lua/d;
%filter_setup
}
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  lua-devel
BuildRequires:  make
BuildRequires:  qt5-qtbase-devel
# /oreon:deps
%description
A utility that converts sourcecode to HTML, XHTML, RTF, LaTeX, TeX,
XSL-FO, XML or ANSI escape sequences with syntax highlighting.
It supports several programming and markup languages.
Language descriptions are configurable and support regular expressions.
The utility offers indentation and reformatting capabilities.
It is easily possible to create new language definitions and colour themes.

%if %{with qt}
%package gui
Summary:        GUI for the highlight source code formatter
Requires:       %{name} = %{version}-%{release}
%description gui
A Qt-based GUI for the highlight source code formatter source.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

CFLAGS="$CFLAGS -fPIC %{optflags}"; export CFLAGS
CXXFLAGS="$CXXFLAGS -fPIC %{optflags}"; export CXXFLAGS
LDFLAGS="$LDFLAGS %{?__global_ldflags}"; export LDFLAGS
 %{__make} all                CFLAGS="${CFLAGS}"          \
                              CXXFLAGS="${CXXFLAGS}"      \
                              LDFLAGS="${LDFLAGS}"        \
                              LFLAGS="-Wl,-O1 ${LDFLAGS}" \
                              PREFIX="%{_prefix}"         \
                              conf_dir="%{_sysconfdir}/"
%if %{with qt}
 %{__make} gui                CFLAGS="${CFLAGS}"          \
                              CXXFLAGS="${CXXFLAGS}"      \
                              LDFLAGS="${LDFLAGS}"        \
                              LFLAGS="-Wl,-O1 ${LDFLAGS}" \
                              PREFIX="%{_prefix}"         \
                              conf_dir="%{_sysconfdir}/" \
                              QMAKE="%{_qt5_qmake}"       \
                              QMAKE_STRIP=
%endif
%install
%make_install PREFIX="%{_prefix}" conf_dir="%{_sysconfdir}/"
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
%if %{with qt}
make install-gui DESTDIR=$RPM_BUILD_ROOT PREFIX="%{_prefix}" conf_dir="%{_sysconfdir}/"
%endif
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}/
desktop-file-install \
    --dir $RPM_BUILD_ROOT%{_datadir}/applications \
   highlight.desktop
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n highlight-gui -f %{oreon_filedir}/highlight-gui.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.19-1
- Prepare for Oreon 11 (RP1)
