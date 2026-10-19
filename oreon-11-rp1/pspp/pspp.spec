%global source1_hash 38e42341381db4e9f4b6f55415084e2b7f54771e2a42098274a1be3cdfb51b2f
%global source0_hash b5e550937bdfa66a1e6ca729195272e8e5e66b3e04686b2d83fb2e66d4ef14c3
Name:           pspp
Version:        2.1.1
Release:        1%{?dist}
Summary:        A program for statistical analysis of sampled data
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/pspp/
VCS:            git://git.savannah.gnu.org/pspp.git
Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz.sig
Source2:        pspp-Smake
Source3:        C2D1AB061656AAC54B5E975485199DE8C6648E90.gpg
Patch:		pspp-0001-Don-t-install-man-page-for-non-existent-app.patch
Patch:		pspp-0002-Revert-update-gnulib-version-to-latest-from-stable-2.patch
Patch:		pspp-0003-MATRIX-Use-int64_t-instead-of-long-for-sequence-rang.patch
Patch:		pspp-0004-Revert-MATRIX-Skip-test-for-too-large-matrices-on-32.patch
Patch:		pspp-0005-Revert-tests-skip-test-MATRIX-very-large-matrices-on.patch
Requires:	hicolor-icon-theme
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cairo-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  gnulib-devel
BuildRequires:  gnupg2
BuildRequires:  gsl-devel
BuildRequires:  gtk3-devel
BuildRequires:  gtksourceview4-devel
BuildRequires:  libpq-devel
BuildRequires:  librsvg2-tools
BuildRequires:  libtool
BuildRequires:  libxml2
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  pango-devel
BuildRequires:  perl(Config::Perl::V)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Diff)
BuildRequires:  perl-devel
BuildRequires:  plotutils-devel
BuildRequires:  python3
BuildRequires:  readline-devel
BuildRequires:  spread-sheet-widget-devel
BuildRequires:  texinfo
BuildRequires:  texlive-tex
BuildRequires:  texlive-wasy
# /oreon:deps
%description
PSPP is a program for statistical analysis of sampled data. It
interprets commands in the SPSS language and produces tabular
output in ASCII, PostScript, or HTML format.

PSPP development is ongoing. It already supports a large subset
of SPSS's transformation language. Its statistical procedure
support is currently limited, but growing.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE3}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
# Remove bundled Gnulib and prepare to import system-wide one
rm -rf gl/
rm -f aclocal.m4
install -D -p -m 0644 %{SOURCE2} Smake

%build

make -f Smake GNULIB=/usr/share/gnulib/lib GNULIB_TOOL=/usr/bin/gnulib-tool
autoreconf -ifv
%configure CFLAGS="${CFLAGS:-%optflags} -fgnu89-inline" \
    --disable-static --disable-rpath
%make_build
%install
%make_install
mkdir -p %{buildroot}%{_pkgdocdir}
cp -p AUTHORS NEWS ONEWS README THANKS %{buildroot}%{_pkgdocdir}
rm %{buildroot}%{_infodir}/dir
find %{buildroot}%{_libdir}/ \
   -name \*.la -delete
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnu.pspp.desktop
%find_lang %{name}
rm -f %{buildroot}%{_datadir}/icons/hicolor/icon-theme.cache
%oreon_autofiles main

%check

make check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
