%global source0_hash 4adb4c243f74d811276529e346deaa064bce28dbfbb837208fc85f2c47b79b30
Name:           R-sass
Version:        %R_rpm_version 0.4.10
Release:        1%{?dist}
Summary:        Syntactically Awesome Style Sheets (Sass)
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=sass&version=%{version}#/sass_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
BuildRequires:  pkgconfig(libsass)
# /oreon:deps
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

%build

%install
%R_install
%R_save_files
%oreon_autofiles main

%check

%R_check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
