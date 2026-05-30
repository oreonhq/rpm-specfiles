%global source0_hash 33f00829263610fd0e73ace9a1137e109435b52ac8f94179a6476d6e784865ff

Name:             adobe-mappings-pdf
Summary:          PDF mapping resources from Adobe
Version:          20190401
Release:          12%{?dist}
License:          BSD-3-Clause

URL:              https://www.adobe.com/
Source:        https://github.com/adobe-type-tools/mapping-resources-pdf/archive/%{version}.tar.gz#/mapping-resources-pdf-%{version}.tar.gz

BuildArch:        noarch
BuildRequires:    git
BuildRequires: make

%description
Mapping resources for PDF have a variety of functions, such as mapping CIDs
(Character IDs) to character codes, or mapping character codes to other
character codes.

These mapping resources for PDF should not be confused with CMap resources.
While both types of resources share the same file structure and syntax, they
have very different functions.

These PDF mapping resources are useful for some applications (e.g. Ghostscript)
to function properly.

# === SUBPACKAGES =============================================================

%package devel
Summary:          RPM macros for Adobe's PDF mapping resources
Requires:         %{name} = %{version}-%{release}

%description devel
This package is useful for development purposes only. It installs RPM
macros useful for building packages against %{name},
as well as all the fonts contained in this font set.


# === BUILD INSTRUCTIONS ======================================================

# NOTE: This package provides only resource files, which are already
#       "pre-compiled" to smallest size possible, but they still remain in
#       postscript format as intended. That's why there is no %%build phase.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n mapping-resources-pdf-%{version} -S git

%install
%make_install prefix=%{_prefix}

# Generate the macro containing the root path to our mappings files:
install -m 0755 -d %{buildroot}%{_rpmconfigdir}/macros.d

cat > %{buildroot}%{_rpmconfigdir}/macros.d/macros.%{name} << _EOF
%%adobe_mappings_rootpath     %{_datadir}/adobe/resources/mapping/
_EOF

# === PACKAGING INSTRUCTIONS ==================================================

%files
%doc README.md
%license LICENSE.txt

%dir %{_datadir}/adobe
%dir %{_datadir}/adobe/resources
%dir %{_datadir}/adobe/resources/mapping

%{_datadir}/adobe/resources/mapping/pdf2other
%{_datadir}/adobe/resources/mapping/pdf2unicode

%files devel
%{_rpmconfigdir}/macros.d/macros.%{name}

# =============================================================================

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 20190401-12
- Prepare for Oreon 11 (RP1)
