%global source0_hash 4dbda173a5acf9b571d7647bbaa6375d73f1eff2d7c8eb531e0b9530b98b0063

Name:           mine_detector
Version:        6.0^20160527
# The version numbering upstream is inconsistent and useless. Here the date of
# the newest source file in the zip file is used to identify the version
Release:        9%{?dist}
Summary:        Mine Detector, a mine-finding game
Summary(sv):    Mine Detector, ett minröjningsspel

License:        GPL-2.0-only
URL:            https://pragmada.x10hosting.com/mindet.html
Source:         https://pragmada.x10hosting.com/MD_1.0-GTK3.zip
Source2:        mine_detector.gpr
Source3:        mine_detector.desktop
# The license file was left out from the zipfile by mistake. Source4 corrects
# this mistake. Sources 5 and 6 clarify the situation.
Source4:        mine_detector-license.txt
Source5:        mine_detector-README.Fedora
Source6:        mine_detector-license_clarification.mbox
# manual page stub:
Source7:        mine_detector.1.en
Source8:        mine_detector.1.sv

BuildRequires:  gcc-gnat GtkAda3-devel desktop-file-utils
BuildRequires:  gprbuild
BuildRequires:  fedora-gnat-project-common
# Build only on architectures where GPRbuild is available:
ExclusiveArch:  %{GPRbuild_arches}

%description
Mine Detector is a mine-finding game with somewhat different rules from other
mine-finding games. Mine Detector rarely requires guessing. Only at the higher
levels may guessing sometimes be the only way to win.

%description -l sv
Mine Detector är ett minröjningsspel med litet annorlunda regler än andra
minröjningsspel. I Mine Detector är det sällan nödvändigt att gissa. Det är
bara på de högre nivåerna som en gissning ibland kan vara det enda sättet att
vinna.

# Disable the hardening hack until someone figures out how to make it work for
# Ada. This game doesn't read any input anyway.
# https://bugzilla.redhat.com/show_bug.cgi?id=1197501
%undefine _hardened_build

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
# -c because there's no top-level directory in the zip file.
cp -p %{SOURCE2} .
cp -p %{SOURCE4} license.txt
cp -p %{SOURCE5} README.Fedora
cp -p %{SOURCE6} license_clarification.mbox

%build
gprbuild -P mine_detector.gpr %{GPRbuild_flags}

%install
mkdir --parents %{buildroot}%{_bindir} \
                %{buildroot}%{_mandir}/man1 %{buildroot}%{_mandir}/sv/man1
cp -p mine_detector %{buildroot}%{_bindir}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE3}
cp -p %{SOURCE7} %{buildroot}%{_mandir}/man1/mine_detector.1
cp -p %{SOURCE8} %{buildroot}%{_mandir}/sv/man1/mine_detector.1

%files
%license license.txt
%license README.Fedora
%license license_clarification.mbox
%{_bindir}/*
%{_datadir}/applications/*
%{_mandir}/man1/*
%{_mandir}/sv/man1/*

%changelog
%autochangelog
