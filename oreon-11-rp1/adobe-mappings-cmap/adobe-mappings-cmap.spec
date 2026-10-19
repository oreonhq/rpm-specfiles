%global source0_hash a88c3beee8d2f139b47f9d7e932ec198be24991dd46fcaef2961b4b5ea855ea2
Name:             adobe-mappings-cmap
Summary:        CMap resources for Adobe's character collections
Version:          20231115
Release:        1%{?dist}
License:          BSD-3-Clause
URL:              https://www.adobe.com/
Source0:        https://github.com/adobe-type-tools/cmap-resources/archive/%{version}.tar.gz#/cmap-resources-%{version}.tar.gz
BuildArch:        noarch
%global crversion %(echo '%{version}' | \
    awk '{print substr($0,1,4)"."substr($0,5,2)"."substr($0,7)}')
Provides:         cmap-resources = %{crversion}-6.%{release}
Obsoletes:        cmap-resources < 2019.07.30-6
Provides:         cmap-resources-cns1-6 = %{crversion}-6.%{release}
Obsoletes:        cmap-resources-cns1-6 < 2019.07.30-6
Provides:         cmap-resources-cns1-7 = %{crversion}-6.%{release}
Obsoletes:        cmap-resources-cns1-7 < 2019.07.30-6
Provides:         cmap-resources-gb1-5 = %{crversion}-6.%{release}
Obsoletes:        cmap-resources-gb1-5 < 2019.07.30-6
Provides:         cmap-resources-japan1-7 = %{crversion}-6.%{release}
Obsoletes:        cmap-resources-japan1-7 < 2019.07.30-6
Provides:         cmap-resources-korea1-2 = %{crversion}-6.%{release}
Obsoletes:        cmap-resources-korea1-2 < 2019.07.30-6
Provides:         cmap-resources-identity-0 = %{crversion}-6.%{release}
Obsoletes:        cmap-resources-identity-0 < 2019.07.30-6
Provides:         cmap-resources-kr-9 = %{crversion}-6.%{release}
Obsoletes:        cmap-resources-kr-9 < 2019.07.30-6
# oreon:deps
BuildRequires:  git
BuildRequires:  make
# /oreon:deps
%description
CMap (Character Map) resources are used to unidirectionally map character codes,
such as Unicode encoding form, to CIDs (Character IDs -- meaning glyphs) of a
CIDFont resource.

These CMap resources are useful for some applications (e.g. Ghostscript) to
correctly display text containing Japanese, (Traditional) Chinese, or Korean
characters.

# === SUBPACKAGES =============================================================

%package deprecated
Summary:          Deprecated CMap resources for Adobe's character collections
Requires:         %{name} = %{version}-%{release}
Provides:         cmap-resources-japan2-0 = %{crversion}-6.%{release}
Obsoletes:        cmap-resources-japan2-0 < 2019.07.30-6
%description deprecated
This sub-package contains currently deprecated CMap resources that some
applications might still require to function properly.

%package devel
Summary:          RPM macros for Adobe's CMap resources for character collections
Requires:         %{name} = %{version}-%{release}
Requires:         %{name}-deprecated = %{version}-%{release}
%description devel
This package is useful for development purposes only. It installs RPM
macros useful for building packages against %{name},
as well as all the fonts contained in this font set.

# === BUILD INSTRUCTIONS ======================================================

# NOTE: This package provides only resource files, which are already
#       "pre-compiled" to smallest size possible, but they still remain in
#       postscript format as intended. That's why there is no %%build phase.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir cmap-resources-%{version}
%oreon_prep
%install
%make_install prefix=%{_prefix}
install -m 0755 -d %{buildroot}%{_rpmconfigdir}/macros.d
cat > %{buildroot}%{_rpmconfigdir}/macros.d/macros.%{name} << _EOF
%%adobe_mappings_rootpath     %{_datadir}/adobe/resources/mapping/
_EOF
%oreon_autofiles adobe-mappings-cmap-deprecated usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles adobe-mappings-cmap-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n adobe-mappings-cmap-deprecated -f %{oreon_filedir}/adobe-mappings-cmap-deprecated.list
%files -n adobe-mappings-cmap-devel -f %{oreon_filedir}/adobe-mappings-cmap-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 20231115-5
- Prepare for Oreon 11 (RP1)
