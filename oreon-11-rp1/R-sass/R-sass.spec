%global source0_hash 4adb4c243f74d811276529e346deaa064bce28dbfbb837208fc85f2c47b79b30

Name:           R-sass
Version:        %R_rpm_version 0.4.10
Release:        %autorelease
Summary:        Syntactically Awesome Style Sheets (Sass)

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
BuildRequires:  pkgconfig(libsass)

%description
An SCSS compiler, powered by the LibSass library. With this, R developers can
use variables, inheritance, and functions to generate dynamic style sheets. The
package uses the Sass CSS extension language, which is stable, powerful, and
CSS compatible.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
cat << EOF > sass/src/Makevars
PKG_LIBS = \$(shell pkgconf --libs libsass)
PKG_CPPFLAGS = \$(shell pkgconf --cflags libsass)
EOF

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
