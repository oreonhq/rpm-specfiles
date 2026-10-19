%global source0_hash fe155709c751b0313e1b4abe747d4bcf10861d54ea6516c4207d56dbaeff9a55
%global forgeurl https://docs.fedoraproject.org/en-US/packaging-guidelines/FontsPolicy/
Epoch: 1
Version: 5.0.0
%forgemeta
%global _spectemplatedir %{_datadir}/rpmdevtools/fedora
%global _docdir_fmt     %{name}
%global ftcgtemplatedir %{_datadir}/fontconfig/templates
%global _fontbasedir            %{_datadir}/fonts
%global _fontconfig_masterdir   %{_sysconfdir}/fonts
%global _fontconfig_confdir     %{_sysconfdir}/fonts/conf.d
%global _fontconfig_templatedir %{_datadir}/fontconfig/conf.avail
BuildArch: noarch
Name:      fonts-rpm-macros
Release:        1%{?dist}
Summary:        Build-stage rpm automation for fonts packages
License:   GPL-3.0-or-later
URL:       https://docs.fedoraproject.org/en-US/packaging-guidelines/FontsPolicy/
Source0:        https://forge.fedoraproject.org/i18n/fonts-rpm-macros/archive/5.0.0.tar.gz#/fonts-rpm-macros-%{version}.tar.gz
Patch0:    0001-avoid-assigning-to-const-lua-variable.patch
Requires:  fonts-srpm-macros = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:  fonts-filesystem  = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:  fontpackages-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: fontpackages-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: fontpackages-tools < %{?epoch:%{epoch}:}%{version}-%{release}
Requires:  fontconfig
Requires:  libappstream-glib
Requires:  uchardet
Requires:  python3-lxml
# oreon:deps

# /oreon:deps
%description
This package provides build-stage rpm automation to simplify the creation of
fonts packages.

It does not need to be included in the default build root: fonts-srpm-macros
will pull it in for fonts packages only.

%package -n fonts-srpm-macros
Summary:   Source-stage rpm automation for fonts packages
Requires:  redhat-rpm-config
%description -n fonts-srpm-macros
This package provides SRPM-stage rpm automation to simplify the creation of
fonts packages.

It limits itself to the automation subset required to create fonts SRPM
packages and needs to be included in the default build root.

The rest of the automation is provided by the fonts-rpm-macros package, that
fonts-srpm-macros will pull in for fonts packages only.

%package -n fonts-filesystem
Summary:   Directories used by font packages
License:   MIT
Provides:  fontpackages-filesystem = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: fontpackages-filesystem < %{?epoch:%{epoch}:}%{version}-%{release}
%description -n fonts-filesystem
This package contains the basic directory layout used by font packages,
including the correct permissions for the directories.

%package -n fonts-rpm-templates
Summary:   Example fonts packages rpm spec templates
License:   MIT
Requires:    fonts-rpm-macros = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: fonts-rpm-macros = %{?epoch:%{epoch}:}%{version}-%{release}
%description -n fonts-rpm-templates
This package contains documented rpm spec templates showcasing how to use the
macros provided by fonts-rpm-macros to create fonts packages.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n fonts-rpm-macros
%patch -P0 -p1
%writevars -f rpm/macros.d/macros.fonts-srpm _fontbasedir _fontconfig_masterdir _fontconfig_confdir _fontconfig_templatedir
for template in templates/rpm/*\.spec ; do
  target=$(echo "${template}" | sed "s|^\(.*\)\.spec$|\1-bare.spec|g")
  grep -v '^%%dnl' "${template}" > "${target}"
  touch -r "${template}" "${target}"
done

%install
install -m 0755 -d    %{buildroot}%{_fontbasedir} \
                      %{buildroot}%{_fontconfig_masterdir} \
                      %{buildroot}%{_fontconfig_confdir} \
                      %{buildroot}%{_fontconfig_templatedir}
install -m 0755 -vd   %{buildroot}%{_spectemplatedir}
install -m 0644 -vp   templates/rpm/*spec \
                      %{buildroot}%{_spectemplatedir}
install -m 0755 -vd   %{buildroot}%{ftcgtemplatedir}
install -m 0644 -vp   templates/fontconfig/*{conf,txt} \
                      %{buildroot}%{ftcgtemplatedir}
install -m 0755 -vd   %{buildroot}%{rpmmacrodir}
install -m 0644 -vp   rpm/macros.d/macros.fonts-* \
                      %{buildroot}%{rpmmacrodir}
install -m 0755 -vd   %{buildroot}%{_rpmluadir}/fedora/srpm
install -m 0644 -vp   rpm/lua/srpm/*lua \
                      %{buildroot}%{_rpmluadir}/fedora/srpm
install -m 0755 -vd   %{buildroot}%{_rpmluadir}/fedora/rpm
install -m 0644 -vp   rpm/lua/rpm/*lua \
                      %{buildroot}%{_rpmluadir}/fedora/rpm
install -m 0755 -vd   %{buildroot}%{_bindir}
install -m 0755 -vp   bin/* %{buildroot}%{_bindir}
%oreon_autofiles fonts-srpm-macros usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles fonts-filesystem usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles fonts-rpm-templates usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n fonts-srpm-macros -f %{oreon_filedir}/fonts-srpm-macros.list
%files -n fonts-filesystem -f %{oreon_filedir}/fonts-filesystem.list
%files -n fonts-rpm-templates -f %{oreon_filedir}/fonts-rpm-templates.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.0.0-3
- Prepare for Oreon 11 (RP1)
