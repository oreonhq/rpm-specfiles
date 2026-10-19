%global source0_hash fd23d279681a6dfe3c15264e33f344045b3ba473da4d19f49e67a50994b077fb
Name:           gifsicle
Version:        1.96
Release:        1%{?dist}
Summary:        Powerful program for manipulating GIF images and animations
License:        GPL-2.0-or-later
URL:            http://www.lcdf.org/gifsicle/
Source0:        http://www.lcdf.org/gifsicle/gifsicle-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires:  make
# /oreon:deps
%description
Gifsicle is a command-line tool for creating, editing, and getting
information about GIF images and animations.

Some more gifsicle features:

    * Batch mode for changing GIFs in place.
    * Prints detailed information about GIFs, including comments.
    * Control over interlacing, comments, looping, transparency...
    * Creates well-behaved GIFs: removes redundant colors, only uses local
      color tables if it absolutely has to (local color tables waste space
      and can cause viewing artifacts), etc.
    * It can shrink colormaps and change images to use the Web-safe palette
      (or any colormap you choose).
    * It can optimize your animations! This stores only the changed portion
      of each frame, and can radically shrink your GIFs. You can also use
      transparency to make them even smaller. Gifsicle?s optimizer is pretty
      powerful, and usually reduces animations to within a couple bytes of
      the best commercial optimizers.
    * Unoptimizing animations, which makes them easier to edit.
    * A dumb-ass name.

One other program is included with gifsicle
and gifdiff compares two GIFs for identical visual appearance.

%package -n gifview
Summary:        Lightweight animated-GIF viewer
%description -n gifview
gifview is a lightweight animated-GIF viewer which can show animations as
slideshows or in real time,

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure
%make_build
%install
%make_install
%oreon_autofiles gifview usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gifview -f %{oreon_filedir}/gifview.list

%changelog

%autochangelog
