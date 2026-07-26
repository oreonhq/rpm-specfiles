%global source0_hash fa56dd08649f51b173017911cae277dc4b2c98211721c2a60708bf1d28839922

%if (0%{?el5} || 0%{?el6})
%global builddolphin 0
%else
%global builddolphin 1
%endif

#global commit #githash for non releases.
#global shortcommit #(c=#{commit}; echo ${c:0:7})

Name:      tnef
Version:   1.4.18
Release:   17%{?dist}
Summary:   Extract files from email attachments like WINMAIL.DAT

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:   GPL-2.0-or-later
# what about: src/ConvertUTF.* ?
# * Unicode, Inc. hereby grants the right to freely use the information
# ... Fedora-legal confirmed this to be the free Unicode license.
# The upstream project has moved to github; 
URL:       https://github.com/verdammelt/tnef
# For git hub release archives:
Source0:   https://github.com/verdammelt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# For git hub tags:
#S#ource0:   https://github.com/verdammelt/%#{name}/archive/%#{commit}/%#{name}-%#{commit}.tar.gz
Source1:   vnd.ms-tnef.desktop
Source2:   tnef-extract.desktop
Source3:   tnefextract.desktop
Source4:   tnef.sh

# Backport from upstream: https://github.com/verdammelt/tnef/commit/86bfa75cfacbe71c8d5282fa0065981b4544c5ad
Patch0:    0000-too-many-arguments.patch

BuildRequires: make
BuildRequires: automake autoconf
BuildRequires: desktop-file-utils

%description
This application provides a way to unpack Microsoft MS-TNEF MIME attachments.
It operates like tar in order to unpack files of type "application/ms-tnef",
which may have been placed into the MS-TNEF attachment instead of being
attached separately.

Such files may have attachment names similar to WINMAIL.DAT

%package nautilus
Summary: Provides TNEF extract extension for Gnome's Nautilus file manager

Requires: tnef
Requires: nautilus

%description nautilus
Provides a right-click extract menu item for Nautilus to extract TNEF files.

%if 0%{builddolphin}
%package dolphin
Summary: Provides TNEF extract extension for KDE's Dolphin file manager

BuildRequires: kf5-rpm-macros
Requires: tnef
Requires: kde-baseapps
Requires: kf5-filesystem

%description dolphin
Provides a right-click extract menu item for Dolphin to extract TNEF files.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
autoreconf -vfi
%configure
%make_build
chmod a-x THANKS

%install
%make_install

mkdir -p %{buildroot}/%{_datadir}/mimelnk/application/
desktop-file-install                                  \
    --dir=%{buildroot}%{_datadir}/mimelnk/application \
%if 0%{?el5}
    --vendor="" \
%endif
    %{SOURCE1}

mkdir -p %{buildroot}/%{_datadir}/applications/
desktop-file-install                           \
    --dir=%{buildroot}%{_datadir}/applications \
%if 0%{?el5}
    --vendor="" \
%endif
    %{SOURCE2}

%if 0%{builddolphin}
mkdir -p %{buildroot}%{_kf5_datadir}/kservices5 
cp %{SOURCE3} %{buildroot}%{_kf5_datadir}/kservices5
%endif

install -p -m 755 %{SOURCE4} \
        %{buildroot}%{_bindir}/

%check
make check DESTDIR=%{buildroot}

%files
%doc AUTHORS ChangeLog COPYING NEWS README.md THANKS
%{_bindir}/%{name}
%{_bindir}/%{name}.sh
%{_mandir}/man1/%{name}.1*

%files nautilus
%{_datadir}/applications/tnef-extract.desktop
%{_datadir}/mimelnk/application/vnd.ms-tnef.desktop

%if 0%{builddolphin}
%files dolphin
%{_kf5_datadir}/kservices5/tnefextract.desktop
%endif

%changelog
%autochangelog
