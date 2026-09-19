%global source0_hash 2be83a4db6510a4848f3abca4540cf54a507aff9215d3bef28003c5d9ca8406e

%global extuuid    system-monitor-next@paradoxxx.zero.gmail.com
%global extdir     %{_datadir}/gnome-shell/extensions/%{extuuid}
%global gschemadir %{_datadir}/glib-2.0/schemas
%global gitname    gnome-shell-system-monitor-next-applet
%global giturl     https://github.com/mgalgs/%{gitname}

%{!?git_post_release_enabled: %global git_post_release_enabled 1}

%if 0%{?git_post_release_enabled}
  # Git commit is needed for post-release version.
  %global gitcommit c4969d993074db75d6d256ace9b845792912d4f9
  %global gitshortcommit %(c=%{gitcommit}; echo ${c:0:7})
  %global gitsnapinfo .20251120git%{gitshortcommit}
%endif

Name:           gnome-shell-extension-system-monitor-applet
Epoch:          1
Version:        38
Release:        41%{?gitsnapinfo}%{?dist}
Summary:        A Gnome shell system monitor extension

# The entire source code is GPLv3+ except convenience.js, which is BSD
License:        GPL-3.0-or-later AND BSD-3-Clause
URL:            https://extensions.gnome.org/extension/3010/system-monitor-next/
Source0:        %{giturl}/archive/%{?gitcommit}%{!?gitcommit:v%{version}}/%{name}-%{version}%{?gitshortcommit:-%{gitshortcommit}}.tar.gz

BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  %{_bindir}/glib-compile-schemas
BuildRequires:  make

Requires:       gnome-shell-extension-common

# CentOS 7 build environment doesn't support Suggests tag.
%if 0%{?fedora} || 0%{?rhel} >= 8
Suggests:       gnome-tweaks
%endif

%description
Display system information in gnome shell status bar, such as memory usage,
CPU usage, and network rate...

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gitname}-%{?gitcommit}%{!?gitcommit:%{version}} -p 1

%build
# Not needed as build target is a dependency of install target in
# upstream Makefile

%install
%make_install VERSION=%{version} PREFIX=%{buildroot}%{_prefix}

# Cleanup unused files.
%{__rm} -fr %{buildroot}%{extdir}/{COPYING*,README*,locale,schemas}

# Install i18n.
%{_bindir}/find %{extuuid} -name '*.po' -print -delete
%{__cp} -pr %{extuuid}/locale %{buildroot}%{_datadir}

# Create manifest for i18n.
%find_lang %{name} --all-name

# CentOS 7 doesn't compile gschemas automatically, Fedora does.
%if 0%{?rhel} && 0%{?rhel} <= 7
%postun
if [ $1 -eq 0 ] ; then
  %{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || :
fi

%posttrans
%{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || :
%endif

%files -f %{name}.lang
%doc README.md
%license COPYING
%{extdir}
%{gschemadir}/*gschema.xml

%changelog
%autochangelog
