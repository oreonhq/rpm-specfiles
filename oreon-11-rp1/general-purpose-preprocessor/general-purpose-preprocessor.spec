%global source0_hash 343d33d562e2492ca9b51ff2cc4b06968a17a85fdc59d5d4e78eed3b1d854b70

Summary: Customizable language-agnostic preprocessor
Name: general-purpose-preprocessor
Version: 2.28
Release: %autorelease
License: LGPL-3.0-or-later
URL: https://logological.org/gpp
Source0: https://files.nothingisreal.com/software/gpp/gpp-%{version}.tar.bz2

BuildRequires: gcc
BuildRequires: make
Provides: gpp

%description
GPP is a general-purpose preprocessor with customizable syntax,
suitable for a wide range of preprocessing tasks. Its independence
from any one programming language makes it much more versatile than
the C preprocessor (cpp), while its syntax is lighter and more
flexible than that of GNU m4. There are built-in macros for use with
C/C++, LaTeX, HTML, XHTML, and Prolog files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n gpp-%{version}

%build
%configure
make

%install
%make_install

%files
%{_bindir}/gpp
%license COPYING THANKS
%doc ChangeLog AUTHORS NEWS README THANKS
%doc %{_mandir}/man1/gpp.1.*
%exclude /usr/share/doc/gpp/gpp.1
%exclude /usr/share/doc/gpp/gpp.html
%exclude /usr/share/doc/gpp/gpp.pp

%changelog
%autochangelog
