%global source0_hash a74ceb1e1803d5ea3a9e550e959d31f05dc91320de0b34cc12ef2b8b34b89d35
%global upstream_name manpages-l10n
%global distribution fedora-rawhide
%global translations \
    cs:    "Czech" \
    da:    "Danish" \
    de:    "German" \
    el:    "Greek" \
    es:    "Spanish" \
    fi:    "Finnish" \
    fr:    "French" \
    hu:    "Hungarian" \
    id:    "Indonesian" \
    it:    "Italian" \
    ko:    "Korean" \
    mk:    "Macedonian" \
    nl:    "Dutch" \
    nb:    "Norwegian Bokmål" \
    pl:    "Polish" \
    pt_BR: "Portuguese (Brazil)" \
    ro:    "Romanian" \
    ru:    "Russian" \
    sr:    "Serbian" \
    sv:    "Swedish" \
    uk:    "Ukrainian" \
    vi:    "Vietnamese"
Name:           man-pages-l10n
Epoch:          3
Version:        4.31.0
Release:        1%{?dist}
Summary:        Translated man pages from the Linux Documentation Project and other software projects
License:        Artistic Licence 2.0 and BSD and BSD with advertising and Copyright only and GFDL and GPL+ and GPLv2 and GPLv2+ and (GPLv2+ or Artistic) and GPLv2 with exceptions and GPLv2+ with exceptions and GPLv3+ and (GPLv3+ and BSD) and (GPLv3+ or BSD) and IJG and ISC and LGPLv2+ and LGPLv3+ and (LGPLv3+ or BSD) and MIT and psutils and Public Domain and Sendmail and Verbatim
URL:            https://manpages-l10n-team.pages.debian.net/manpages-l10n/
Source0:        https://salsa.debian.org/%{upstream_name}-team/%{upstream_name}/-/archive/%{version}/%{upstream_name}-%{version}.tar.bz2
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  po4a
# /oreon:deps
%description
Translated man pages from the Linux Documentation Project
and other software projects.

# generate subpackages
%{lua: for code, name in rpm.expand('%{translations}'):gmatch('(%S+):%s+(%b"")') do
    name = name:gsub('"', '')

    print('%package -n man-pages-' .. code .. '\n')
    print('Summary: ' .. name .. ' man pages from the Linux Documentation Project\n')
    print('Requires: man-pages-reader\n')
    print('Supplements: (man-pages and langpacks-' .. code .. ')\n')

    -- obsolete man-pages-es-extra
    if code == 'es' then
        print('Obsoletes: man-pages-es-extra < 1.55-36\n')
    end

    print('%description -n man-pages-' .. code .. '\n')
    print('Manual pages from the Linux Documentation Project, translated into ' .. name .. '.\n')
end}

%prep

%autosetup -p1 -n %{upstream_name}-%{version}

%build

%configure --enable-distribution=%{distribution}
%make_build
%install
%make_install
rm %{buildroot}%{_mandir}/de/man5/ethers.5*
%{lua: for code in rpm.expand('%{translations}'):gmatch('(%S+):%s+%b""') do
    print('%files -n man-pages-' .. code .. '\n')
    print('%license LICENSE COPYRIGHT.md\n')
    print('%doc AUTHORS.md CHANGES.md README.md\n')
    print(rpm.expand('%{_mandir}') .. '/' .. code .. '/man*/*\n')
end}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n man-pages-cs -f %{oreon_filedir}/man-pages-cs.list
%files -n man-pages-da -f %{oreon_filedir}/man-pages-da.list
%files -n man-pages-de -f %{oreon_filedir}/man-pages-de.list
%files -n man-pages-el -f %{oreon_filedir}/man-pages-el.list
%files -n man-pages-es -f %{oreon_filedir}/man-pages-es.list
%files -n man-pages-fi -f %{oreon_filedir}/man-pages-fi.list
%files -n man-pages-fr -f %{oreon_filedir}/man-pages-fr.list
%files -n man-pages-hu -f %{oreon_filedir}/man-pages-hu.list
%files -n man-pages-id -f %{oreon_filedir}/man-pages-id.list
%files -n man-pages-it -f %{oreon_filedir}/man-pages-it.list
%files -n man-pages-ko -f %{oreon_filedir}/man-pages-ko.list
%files -n man-pages-mk -f %{oreon_filedir}/man-pages-mk.list
%files -n man-pages-nl -f %{oreon_filedir}/man-pages-nl.list
%files -n man-pages-nb -f %{oreon_filedir}/man-pages-nb.list
%files -n man-pages-pl -f %{oreon_filedir}/man-pages-pl.list
%files -n man-pages-pt_BR -f %{oreon_filedir}/man-pages-pt_BR.list
%files -n man-pages-ro -f %{oreon_filedir}/man-pages-ro.list
%files -n man-pages-ru -f %{oreon_filedir}/man-pages-ru.list
%files -n man-pages-sr -f %{oreon_filedir}/man-pages-sr.list
%files -n man-pages-sv -f %{oreon_filedir}/man-pages-sv.list
%files -n man-pages-uk -f %{oreon_filedir}/man-pages-uk.list
%files -n man-pages-vi -f %{oreon_filedir}/man-pages-vi.list

%changelog

%autochangelog
