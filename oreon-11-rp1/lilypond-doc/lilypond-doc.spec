%global source0_hash none

Name:           lilypond-doc
Version:        2.25.35
Release:        1%{?dist}
Summary:        HTML documentation for LilyPond

License:        GPL-3.0-only
URL:            https://lilypond.org
Source0:        https://gitlab.com/lilypond/lilypond/-/releases/v%{version}/downloads/lilypond-%{version}-documentation.tar.xz
BuildArch:      noarch

%description
LilyPond is an automated music engraving system. It formats music
beautifully and automatically, and has a friendly syntax for its input
files.

This package contains the HTML documentation for LilyPond.

%prep
%setup -q -c

%build

%install
mkdir -p $RPM_BUILD_ROOT

%files
%license share/doc/lilypond/html/COPYING*
%doc share/doc/lilypond/html/Documentation

%changelog
%autochangelog
