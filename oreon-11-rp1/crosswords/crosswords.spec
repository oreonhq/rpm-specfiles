%global source0_hash 493623de5aa3c4ee1a465ae41ffd389d365f72af87afcd0e2ef66a90d45a76e9
%bcond docs 1
%bcond tests 1
%global ipuz_soversion 0.5
Name:           crosswords
Version:        0.3.18.1
Release:        1%{?dist}
Summary:        Solve crossword puzzles
License:        GPL-3.0-or-later AND CC-BY-SA-4.0 AND LicenseRef-Fedora-UltraPermissive AND MIT
URL:            https://gitlab.gnome.org/jrb/crosswords
Source0:        https://gitlab.gnome.org/jrb/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    s390x
%if %{with docs}
%endif
%if %{with tests}
%endif
Requires:       dbus-common
Requires:       %{name}-puzzle-sets-cats-and-dogs = %{version}-%{release}
Requires:       %{name}-puzzle-sets-uri = %{version}-%{release}
Recommends:     %{name}-thumbnailer = %{version}-%{release}
Suggests:       crossword-editor = %{version}-%{release}
%if %{with docs}
Suggests:       %{name}-doc = %{version}-%{release}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-crosswords = %{version}-%{release}
# /oreon:deps
%description
A simple and fun game of crosswords. Load your crossword files, or play one of
the included games. Features include:

- Support for shaped and colored crosswords
- Loading .ipuz and .puz files
- Hint support, such as showing mistakes and suggesting words
- Dark mode support
- Locally installed crosswords as well as support for 3rd party downloaders

%package        puzzle-sets-cats-and-dogs
Summary:        Puzzles about cats and dogs for GNOME Crosswords
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description    puzzle-sets-cats-and-dogs
This package contains a puzzle set about cats and dogs for GNOME Crosswords.

%package        puzzle-sets-internal
Summary:        Load additional puzzles for GNOME Crosswords
Requires:       %{name} = %{version}-%{release}
Provides:       crosswords-puzzle-sets-uri = %{version}-%{release}
Obsoletes:      crosswords-puzzle-sets-uri < 0.3.6-3
BuildArch:      noarch
Recommends:     ipuz-convertor = %{version}-%{release}
%description    puzzle-sets-internal
This package contains puzzle sets used internally by GNOME Crosswords to load
additional puzzles from disk.

%package        thumbnailer
Summary:        GNOME Crosswords Thumbnailer
%description    thumbnailer
This package provides a thumbnailer for crosswords puzzles in formats supported
by GNOME Crosswords.

%if %{with docs}
%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
%description    doc
This package contains additional documentation for GNOME Crosswords.
%endif

%package -n     crossword-editor
Summary:        Crossword puzzle editor
Requires:       %{name}%{?_isa} = %{version}-%{release}
Recommends:     %{name}-thumbnailer = %{version}-%{release}
Recommends:     ipuz-convertor = %{version}-%{release}
Suggests:       ipuz2pdf = %{version}-%{release}
%description -n crossword-editor
Standalone-tool to create crossword puzzles based on GNOME Crosswords. It can
be used to create simple puzzles with grids and clues. It has a pattern solver
and grid autofill dialog for filling in hard-to-finish corners, and will make
suggestions of words when creating the grid.

%package -n     ipuz-convertor
Summary:        Converts puz files to ipuz files
BuildArch:      noarch
Requires:       crosswords
Requires:       python3
Requires:       python3dist(beautifulsoup4)
Requires:       python3dist(dateparser)
Requires:       python3dist(lxml)
Requires:       python3dist(puzpy)
Requires:       python3dist(regex)
Requires:       python3dist(requests)
Requires:       python3dist(xdfile)
%description -n ipuz-convertor
ipuz-convertor is a script to convert puzzle files from puz to ipuz.

%package -n     ipuz2pdf
Summary:        Export IPUZ puzzles to printable PDF documents
%description -n ipuz2pdf
ipuz2pdf is a tool to export IPUZ puzzles to printable PDF documents.

%prep

%autosetup -p1

# Relax regex version pin
sed -i 's:^regex==.*$:regex:' requirements.txt

# Update image references in README
mkdir images
cp -p data/images/{a-dogs-day,hero}.png images/
sed -i 's:data/images/:images/:g' README.md

# Relax lxml version pin on older releases

# Generate Python dependencies for the converter
%build

%meson -Ddevelopment=false
%meson_build
%if %{with docs}
sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}
%endif
%install
%meson_install
%find_lang %{name}
rm -f %{buildroot}%{_libexecdir}/gen-word-list-resource
%oreon_autofiles crosswords-puzzle-sets-cats-and-dogs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles crosswords-puzzle-sets-internal usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles crosswords-thumbnailer usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles crosswords-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles crossword-editor usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ipuz-convertor usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ipuz2pdf usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with tests}
%check

%meson_test
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/org.gnome.Crosswords.metainfo.xml
desktop-file-validate \
  %{buildroot}/%{_datadir}/applications/org.gnome.Crosswords.desktop \
  %{buildroot}/%{_datadir}/applications/org.gnome.Crosswords.Editor.desktop
%endif
%files
%files -n crosswords-puzzle-sets-cats-and-dogs -f %{oreon_filedir}/crosswords-puzzle-sets-cats-and-dogs.list
%files -n crosswords-puzzle-sets-internal -f %{oreon_filedir}/crosswords-puzzle-sets-internal.list
%files -n crosswords-thumbnailer -f %{oreon_filedir}/crosswords-thumbnailer.list
%files -n crosswords-doc -f %{oreon_filedir}/crosswords-doc.list
%files -n crossword-editor -f %{oreon_filedir}/crossword-editor.list
%files -n ipuz-convertor -f %{oreon_filedir}/ipuz-convertor.list
%files -n ipuz2pdf -f %{oreon_filedir}/ipuz2pdf.list

%changelog

%autochangelog
