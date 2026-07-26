%global source0_hash 36a0a60e422907b2baead8b82cec56008240b7a950678294bb2e1df65e1a6bb3

%global framework kdoctools

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Name:    kf5-%{framework}
Version: 5.116.0
Release: 5%{?dist}
Summary: KDE Frameworks 5 Tier 2 addon for generating documentation

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0:        http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-karchive-devel >= %{majmin}
BuildRequires:  kf5-ki18n-devel >= %{majmin}

BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
%if 0%{?fedora} || 0%{?rhel} > 7
%global _with_html --with-html
BuildRequires:  perl-generators
%endif
%if 0%{?fedora} || 0%{?epel} > 7
%global perl_uri_escape perl(Any::URI::Escape)
%else
%global perl_uri_escape perl(URI::Escape)
%endif
BuildRequires:  %{perl_uri_escape}
BuildRequires:  qt5-qtbase-devel

Requires:       docbook-dtds
Requires:       docbook-style-xsl

%description
Provides tools to generate documentation in various format from DocBook files.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       kf5-kdoctools-static = %{version}-%{release}
Requires:       qt5-qtbase-devel
Requires:       %{perl_uri_escape}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf5 \
    %{?tests:-DBUILD_TESTING:BOOL=ON}

%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name --with-man %{?_with_html}

%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
make test -C %{_target_platform} ARGS="--output-on-failure --timeout 300" ||:
%endif

%ldconfig_scriptlets

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf5_libdir}/libKF5DocTools.so.5*
## FIXME/TODO: which of these to move to -devel -- rex
%{_kf5_bindir}/checkXML5
%{_kf5_bindir}/meinproc5
%{_kf5_mandir}/man1/*.1*
%{_kf5_mandir}/man7/*.7*
%{_kf5_datadir}/kf5/kdoctools/
%if !0%{?_with_html:1}
%{_kf5_docdir}/HTML/*/kdoctools5-common/
%endif

%files devel
%{_kf5_includedir}/KDocTools/
%{_kf5_libdir}/libKF5DocTools.so
%{_kf5_libdir}/cmake/KF5DocTools/

%changelog
%autochangelog
