%global source0_hash a2de62696aba2c60fd46b9ccdd489e179b241b4930f8ba51fdb4a870f4c1090b

%global pkg     proofgeneral
%global giturl  https://github.com/ProofGeneral/PG

# Get post-4.5 release bug fixes and support for prooftree 0.14
%global commit  1ffca70b2fcfd1c524f9b9e5ceebae07d3b745b6
%global date    20240912
%global forgeurl %{giturl}

Name:           emacs-common-%{pkg}
Version:        4.5
Summary:        Emacs mode for standard interaction interface for proof assistants

%forgemeta

# The code is GPL-3.0-or-later.
# The icons are CC-BY-SA-3.0, except for the search icon.
# The search icon is CC-BY-SA-2.0.
License:        GPL-3.0-or-later AND CC-BY-SA-3.0 AND CC-BY-SA-2.0
Release:        14%{?dist}
URL:            https://proofgeneral.github.io/
VCS:            git:%{giturl}.git
Source0:        %{forgesource}
Source1:        io.github.%{pkg}.metainfo.xml
# Backwards compatibility shell script launcher
Source2:        %{pkg}
# Additional icon sizes created with gimp from icons in the source file
Source3:        %{pkg}-96x96.png
Source4:        %{pkg}-256x256.png

# Patch 0 - Fedora specific, don't do an "install-info" in the make process
# (which would occur at build time), but instead put it into a scriptlet
Patch:          pg-4.2-Makefile.patch

# Bring the desktop file up to date with current standards.
Patch:          pg-4.2-desktop.patch

# Fix some places where looking-back is called without enough arguments
Patch:          pg-4.5-looking-back.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  emacs-nox
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  texlive-cm-super
BuildRequires:  texlive-ec
BuildRequires:  texinfo-tex

Requires:       hicolor-icon-theme

Recommends:     prooftree

%description
Proof General is a generic front-end for proof assistants (also known as
interactive theorem provers) based on Emacs.

Proof General allows one to edit and submit a proof script to a proof
assistant in an interactive manner:
- It tracks the goal state, and the script as it is submitted, and allows for
  easy backtracking and block execution.
- It adds toolbars and menus to Emacs for easy access to proof assistant
  features.
- It integrates with Emacs Unicode support for some provers to provide output
  using proper mathematical symbols.
- It includes utilities for generating Emacs tags for proof scripts, allowing
  for easy navigation.

Proof General supports a number of different proof assistants (Isabelle, Coq,
PhoX, and LEGO to name a few) and is designed to be easily extendable to work
with others.

%package -n emacs-%{pkg}
Summary:        Compiled elisp files to run Proof General under GNU Emacs
Requires:       emacs(bin) %{?_emacs_version:>= %{_emacs_version}}
Requires:       emacs-common-%{pkg} = %{version}-%{release}

%description -n emacs-%{pkg}
Proof General is a generic front-end for proof assistants based on Emacs.

This package contains the byte compiled elisp packages to run Proof General
with GNU Emacs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p0

%conf
fixtimestamp() {
  touch -r $1.orig $1
  rm -f $1.orig
}

# Fix rpmlint complaints:
# Remove .cvsignore files
find . -name .cvsignore -delete

# Fix non UTF-8 documentation and theory files
for f in phox/sqrt2.phx; do
  mv $f $f.orig
  iconv -f iso-8859-1 -t utf8 $f.orig > $f
  fixtimestamp $f
done

%build
# Make full copies of emacs versions, set options in the proofgeneral start
# script
make clean
make EMACS=emacs compile bashscripts perlscripts doc

%install
%define full_doc_dir %{_datadir}/doc/%{pkg}
%define full_man_dir %{_mandir}/man1

%define doc_options DOCDIR=%{buildroot}%{full_doc_dir} MANDIR=%{buildroot}%{full_man_dir} INFODIR=%{buildroot}%{_infodir}
%define common_options PREFIX=%{buildroot}%{_prefix} DEST_PREFIX=%{_prefix} DESKTOP=%{buildroot}%{_datadir} BINDIR=%{buildroot}%{_bindir} %{doc_options}

%define emacs_options ELISP_START=%{buildroot}%{_emacs_sitestartdir} ELISP=%{buildroot}%{_emacs_sitelispdir}/%{pkg} DEST_ELISP=%{_emacs_sitelispdir}/%{pkg}

make EMACS=emacs %{common_options} %{emacs_options} install install-doc

# Do not install the INSTALL or COPYING files
rm %{buildroot}%{full_doc_dir}/{COPYING,INSTALL}

# Validate the desktop file
desktop-file-validate %{buildroot}%{_datadir}/applications/proofgeneral.desktop

# Install the AppData file
mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 %{SOURCE1} %{buildroot}%{_metainfodir}
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/io.github.%{pkg}.metainfo.xml

# Install the backwards compatibility launcher
cp -p %{SOURCE2} %{buildroot}%{_bindir}

# Install additional icon sizes
install -Dpm 644 %{SOURCE3} \
  %{buildroot}%{_datadir}/icons/hicolor/96x96/apps/%{pkg}.png
install -Dpm 644 %{SOURCE4} \
  %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{pkg}.png

%files
%license COPYING
%{full_doc_dir}
%{full_man_dir}/*
%{_infodir}/*
%{_bindir}/*
%{_datadir}/application-registry/%{pkg}.applications
%{_datadir}/applications/%{pkg}.desktop
%{_datadir}/icons/hicolor/*/apps/%{pkg}.png
%{_datadir}/mime-info/%{pkg}.*
%{_metainfodir}/io.github.%{pkg}.metainfo.xml

%files -n emacs-%{pkg}
%{_emacs_sitestartdir}/*.el
%{_emacs_sitelispdir}/%{pkg}/

%changelog
%autochangelog
