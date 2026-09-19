%global source0_hash 8654c861a058ae1c81dd23e5022a09007dcda0bb95fb0072d84bd2e2b0b67732

Name:           sugar-view-slides
Version:        15
Release:        11%{?dist}
Summary:        Image series viewer for Sugar

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://wiki.sugarlabs.org/go/Activities/View_Slides
Source0:        http://download.sugarlabs.org/sources/honey/ViewSlides/ViewSlides-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  python3 python3-devel
BuildRequires:  sugar-toolkit-gtk3
BuildRequires:  gettext

Requires:       sugar >= 0.116
Requires:       python3-pygame

%description
The View Slides activity is meant to allow the XO laptop to read
view the contents of a Zip file containing images named sequentially.
Project Gutenberg has a few books as raw scanned images, and this can
be a useful format for picture books, comic books, magazine articles,
photo essays, etc.

The interface to View Slides is similar to the core Read activity,
which should not be surprising as the toolbar code was adapted from
Read's toolbar. You can use the up and down arrows or the game
controller to move from page to page.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n ViewSlides-%{version}

sed -i 's/python/python3/' *.py

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}%{_datadir}/{sugaractivitydir}/ViewSlides.activity/

%find_lang org.laptop.ViewSlidesActivity

%files -f org.laptop.ViewSlidesActivity.lang
%doc README.md
%{sugaractivitydir}/ViewSlides.activity/

%changelog
%autochangelog
