%global source0_hash 72ec66a7ac126f2bff66f2f9957923214d296f69843034fc3f27eabc036b7031
Version: 2.600
Release:        1%{?dist}
%global foundry           SIL
%global fontlicense       OFL-1.1-RFN
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}
%global fontfamily        Tai Heritage Pro
%global fontsummary       Tai Heritage Pro, a traditional style Tai Viet script font family
%global projectname       %{lua:t=string.gsub(rpm.expand("%{fontfamily}"), " SIL$", ""); t=string.gsub(t, "[%p%s]+", ""); print(string.lower(t))}
%global archivename       %{lua:t=string.gsub(rpm.expand("%{fontfamily}"), "[%p%s]+", ""); print(t)}-%{version}
URL:                      https://software.sil.org/taiheritage/
%global fonts             *.ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
The Tai people of northwestern Vietnam and surrounding areas have a long
tradition of literacy in the Tai Viet script. Tai Heritage Pro reflects the
traditional style of this script.}
Source0:        https://github.com/silnrsi/font-taiheritagepro/releases/download/v%{version}/TaiHeritagePro-%{version}.tar.xz
Source10: 65-%{fontpkgname}.xml
%fontpkg
# oreon:deps
BuildRequires:  fonts-rpm-macros
# /oreon:deps
%package doc
Summary:   Optional documentation files of %{name}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{archivename}
%linuxtext *txt documentation/*txt documentation/developer/*txt

%build

%fontbuild
%install
%fontinstall
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%fontcheck
%fontfiles
%files -f %{oreon_filedir}/main.list
%files -n bitmap-ecolier-court-fonts-doc -f %{oreon_filedir}/bitmap-ecolier-court-fonts-doc.list

%changelog

%autochangelog
