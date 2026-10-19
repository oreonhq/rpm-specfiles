%global source0_hash f355758d8e97271265e7e2e03b5e57e7fcaeb0acdac2c8857ad80733400846b5
%global fontname   baekmuk-bdf
%global catalogue    %{_sysconfdir}/X11/fontpath.d
Version: 2.2
Release:        44%{?dist}
URL:     http://kldp.net/projects/baekmuk/
%global foundry           Baekmuk
%global fontlicense       Baekmuk
%global fontlicenses      COPYRIGHT COPYRIGHT.ko
%global fontdocs          README
%global fontdocsex        %{fontlicenses}
%global fontfamily        Baekmuk BDF
%global fontsummary       Korean bitmap fonts
%global fonts             bdf/*.pcf.gz
%global fontdescription   %{expand:
This package provides the Korean Baekmuk bitmap fonts.
}
%global fontappstreams    %{SOURCE1}
Source0:        http://kldp.net/frs/download.php/1428/%{fontname}-%{version}.tar.gz
Source1:  org.fedoraproject.baekmuk-bdf-fonts.metainfo.xml
Patch0:   baekmuk-bdf-fonts-fix-fonts-alias.patch
%fontpkg
# oreon:deps
BuildRequires:  bdftopcf
BuildRequires:  fonts-rpm-macros
BuildRequires:  mkfontdir
# /oreon:deps
%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{fontname}-%{version}

%build

for file in bdf/*.bdf; do
    bdftopcf $file | gzip -9 > ${file%.bdf}.pcf.gz
done
%fontbuild
%install
%fontinstall
install -d $RPM_BUILD_ROOT%{catalogue}
ln -sf ../../..%{fontdir} $RPM_BUILD_ROOT%{catalogue}/%{name}
mkfontdir $RPM_BUILD_ROOT%{fontdir} 
iconv -f EUC-KR -t UTF-8 COPYRIGHT.ks > COPYRIGHT.ko
install -m 0444 bdf/fonts.alias $RPM_BUILD_ROOT%{fontdir}/
%oreon_autofiles main

%check

%fontcheck
%fontfiles
%verify(not md5 size mtime) %{fontdir}/fonts.dir
%{fontdir}/fonts.alias
%{catalogue}/%{name}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
