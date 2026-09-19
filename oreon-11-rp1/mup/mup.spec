%global source0_hash 5db7c8b12cc4edcc1d2b40e53b24bc3c425b04673b0e86b51c62ec55fc7665a6

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:           mup
Version:        7.2

Release:        4%{?dist}
Summary:        A music notation program that can also generate MIDI files
License:        Mup
URL:            http://www.arkkra.com/doc/overview.html

%define         versionnodot %(echo %{version} | tr -d ".")

Source0:        http://www.arkkra.com/ftp/pub/unix/mup%{versionnodot}src.tar.gz
Source1:        mupmate.desktop

# Newer Fedora build roots no longer include, gcc, gcc-c++ by default
# https://fedoraproject.org/wiki/Packaging:C_and_C%2B%2B
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make

BuildRequires:  glibc-devel
BuildRequires:  fltk-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXext-devel
BuildRequires:  libXpm-devel
BuildRequires:  libXft-devel
BuildRequires:  desktop-file-utils
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  man-db

%description
Mup is a program for printing music. It takes an input file containing ordinary
(ASCII) text describing music, and produces PostScript output for printing the
musical score described by the input.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# Preserve the timestamp of files that we copy from the Mup source tree
sed -i -e 's|cp |cp -p |' simple.makefile

%build
# Use -std=gnu17 to work around build issues with C23 that gcc 15 defaults to
%global optflags %optflags -std=gnu17
make %{?_smp_mflags} CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" LIBDIR="%{_datadir}/%{name}" DOCDIR="%{_pkgdocdir}" -f simple.makefile

%install
rm -rf %{buildroot}
make DESTDIR="%{buildroot}" LIBDIR="%{buildroot}%{_datadir}/%{name}" DOCDIR="%{buildroot}%{_pkgdocdir}" install -f simple.makefile

# License is handled separately
rm "%{buildroot}%{_pkgdocdir}/license.txt"

# Add docs that aren't installed by make install
cp -a AUTHORS ChangeLog NEWS README "%{buildroot}%{_pkgdocdir}"/.

# Remove docs that are not applicable
rm "%{buildroot}%{_pkgdocdir}/Macinst.html"
rm "%{buildroot}%{_pkgdocdir}/winrun.html"

mkdir -p %{buildroot}/%{_datadir}/applications
cp -p %{SOURCE1} %{buildroot}/%{_datadir}/applications/
desktop-file-validate %{buildroot}/%{_datadir}/applications/mupmate.desktop

%files
%license LICENSE
%{_pkgdocdir}/*
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/mup
%{_datadir}/applications/*
%{_datadir}/pixmaps/*

%changelog
%autochangelog
