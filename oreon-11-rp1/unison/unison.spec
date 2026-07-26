%global source0_hash a259537cef465c4806d6c1638c382620db2dd395ae42a0dd2efa3ba92712bed5

%bcond doc 1
%bcond gtk 1

%ifarch %{ocaml_native_compiler}
%global native true
%else
%global native false
%endif

# OCaml i686 support was dropped in OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

Name:           unison
Version:        2.53.7
Release:        5%{?dist}
Summary:        File Synchronizer

%global         forgeurl https://github.com/bcpierce00/%{name}/
%global         tag v%{version}
%forgemeta

# LGPL-2.0-only
#   src/ubase/myMap.ml{,i}
#   src/ubase/uarg.ml{,i}
# LGPL-2.1-only
#   src/fsmonitor/inotify/inotify.ml{,i}
#   src/fsmonitor/inotify/inotify_stubs.c
#   src/hash_compat.c
# LGPL-2.1-or-later
#   src/lwt
License:        GPL-3.0-or-later AND LGPL-2.0-only AND LGPL-2.1-only AND LGPL-2.1-or-later
URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        %{name}.desktop
Source2:        %{name}.metainfo.xml

BuildRequires:  ocaml
BuildRequires:  ocaml-findlib

%if %{with gtk}
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  libappstream-glib
BuildRequires:  ocaml-lablgtk3-devel
BuildRequires:  ocaml-cairo-devel
%endif
%if %{with doc}
BuildRequires:  hevea
BuildRequires:  lynx
BuildRequires:  tex-ec
BuildRequires:  tex-latex
%endif

Provides:       bundled(ocaml-inotify)

%description
Unison is a file-synchronization tool for POSIX-compliant systems (e.g. *BSD,
GNU/Linux, macOS) and Windows. It allows two replicas of a collection of files
and directories to be stored on different hosts (or different disks on the same
host), modified separately, and then brought up to date by propagating the
changes in each replica to the other.

%if %{with gtk}
%package        gtk
Summary:        Unison File Synchronizer GTK interface
Requires:       hicolor-icon-theme
%description    gtk
%{summary}.
%endif

%if %{with doc}
%package        doc
Summary:        Unison File Synchronizer documentation
BuildArch:      noarch
%description    doc
%{summary}.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup

%build
%make_build        \
  NATIVE=%{native} \
  tui              \
  fsmonitor        \
  manpage

%if %{with gtk}
%make_build        \
  NATIVE=%{native} \
  gui
%endif

%if %{with doc}
%make_build        \
  NATIVE=%{native} \
  docs
%endif

%install
%make_install       \
  NATIVE=%{native}  \
  PREFIX=%{_prefix}

%if %{with gtk}
# Install the various icons according to the "Icon Theme Specification"
# https://specifications.freedesktop.org/icon-theme-spec/icon-theme-spec-latest.html
for size in 16 24 32 48 256; do
  format="${size}x${size}"
  install -Dpm0644 icons/U.${format}x16m.png \
    %{buildroot}%{_datadir}/icons/hicolor/${format}/apps/%{name}.png
done
install -Dpm0644 icons/U.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}
install -Dpm0644 -t %{buildroot}%{_metainfodir} %{SOURCE2}
%endif

%if %{with doc}
install -Dpm0644 -t %{buildroot}%{_docdir}/%{name} doc/%{name}-manual.{html,pdf,txt}
%endif

%check
make test          \
  NATIVE=%{native}
%if %{with gtk}
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
%endif

%files
%doc NEWS.md README.md
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/%{name}-fsmonitor
%{_mandir}/man1/%{name}.1*

%if %{with gtk}
%files          gtk
%license LICENSE
%{_bindir}/%{name}-gui
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_metainfodir}/%{name}.metainfo.xml
%endif

%if %{with doc}
%files          doc
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/%{name}-manual.{html,pdf,txt}
%endif

%changelog
%autochangelog
