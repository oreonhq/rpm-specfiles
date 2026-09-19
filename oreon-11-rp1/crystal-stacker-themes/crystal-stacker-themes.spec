%global source0_hash 16637236bc6fccee351d8f53cbb875f9e7b802f3479305f10fb6fc9bc496d16d

Name:           crystal-stacker-themes
Version:        1.0
Release:        36%{?dist}
Summary:        Themes for the Crystal Stacker game
# Automatically converted from old format: Crystal Stacker - review is highly recommended.
License:        CrystalStacker
URL:            http://www.t3-i.com/cstacker.htm
Source0:        http://ncdgames.t3-i.com/csdream.zip
Source1:        http://ncdgames.t3-i.com/csfood.zip
Source2:        http://ncdgames.t3-i.com/csgems.zip
Source3:        http://ncdgames.t3-i.com/cslcd.zip
Source4:        http://ncdgames.t3-i.com/csmatrix.zip
Source5:        http://ncdgames.t3-i.com/csoldcs.zip
Source6:        http://ncdgames.t3-i.com/csstone.zip
Source7:        crystal-stacker-theme-license.txt
Source8:        cs-readme.txt
BuildArch:      noarch
Requires:       crystal-stacker

%description
7 new / extra themes for the Crystal Stacker game.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -a5 -a6
# don't pass these to %%setup, their filenames must be forced to lowercase
unzip -qqLL %{SOURCE1}
unzip -qqLL %{SOURCE2}
unzip -qqLL %{SOURCE3}
unzip -qqLL %{SOURCE4}
# put these somewhere were %%doc can find them
cp %{SOURCE7} %{SOURCE8} .

%build
# nothing to build datafiles only

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/crystal-stacker
install -p -m 644 *.xm *.cth $RPM_BUILD_ROOT%{_datadir}/crystal-stacker

%files
%doc crystal-stacker-theme-license.txt cs-readme.txt
%{_datadir}/crystal-stacker/*.xm
%{_datadir}/crystal-stacker/*.cth

%changelog
%autochangelog
