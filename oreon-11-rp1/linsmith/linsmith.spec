%global source0_hash d6c9c9b5b1f89b19ad1a9a0630f11009eefcea0a6a7f88fcbbc96bc592b84998

Name:           linsmith
Version:        0.99.33
Release:        %autorelease
Summary:        A Smith charting program
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://jcoppens.com/soft/linsmith/index.en.php
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libgnomeui-devel
BuildRequires:  make
Requires:       electronics-menu
Requires:       tcl

%description
linSmith is a Smith Charting program.
It's main features are:
  * Definition of multiple load impedances
  * Addition of discrete and line components
  * A 'virtual' component switches from impedance
    to admittance to help explaining parallel components
  * The chart works in real impedances
  * Load and circuit configuration is stored separately,
    permitting several solutions without re-defining the other

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
# Build in C89 mode due to many implicit function declarations.
%global build_type_safety_c 0
%set_build_flags
CC="$CC -std=gnu89"
export CPPFLAGS="$CPPFLAGS -fcommon"
%configure
%make_build

%install
%make_install

desktop-file-install \
    --dir=%{buildroot}/%{_datadir}/applications \
    --delete-original                           \
    --remove-category GTK                       \
    --remove-category GNOME                     \
    --add-category "Electronics"                \
    %{_builddir}/%{name}-%{version}/%{name}.desktop

# icon
cp -p linsmith_icon.xpm %{buildroot}/%{_datadir}/pixmaps/%{name}/

# man file
%{__mkdir} -p %{buildroot}/%{_datadir}/man/man1
cp -p doc/linsmith.1 %{buildroot}/%{_datadir}/man/man1

#examples
mv %{buildroot}/%{_datadir}/%{name} examples/

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README THANKS doc/manual.pdf examples/*
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/pixmaps/%{name}
%{_datadir}/man/man1/%{name}.1.gz

%changelog
%autochangelog
