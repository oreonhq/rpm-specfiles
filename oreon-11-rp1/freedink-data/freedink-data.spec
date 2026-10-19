%global source0_hash 715f44773b05b73a9ec9b62b0e152f3f281be1a1512fbaaa386176da94cffb9d
Name:		freedink-data
Version:	1.08.20190120
Release:        1%{?dist}
Summary:        Adventure and role-playing game (assets)
License:	Zlib AND CC-BY-SA-3.0 AND GPL-2.0-or-later
URL:		https://www.gnu.org/software/freedink/
Source0:        https://ftp.gnu.org/gnu/freedink/%{name}-%{version}.tar.gz
BuildArch:	noarch
# oreon:deps
BuildRequires:  make
# /oreon:deps
%description
Dink Smallwood is an adventure/role-playing game, similar to Zelda,
made by RTsoft. Besides twisted humor, it includes the actual game
editor, allowing players to create hundreds of new adventures called
Dink Modules or D-Mods for short.

This package contains architecture-independent data for the original
game, along with free sound and music replacements.

%prep

%setup -q
# Strip DOS EOL from documentation
# https://fedoraproject.org/wiki/PackageMaintainers/Common_Rpmlint_Issues#wrong-file-end-of-line-encoding
sed -i 's/\r//' README.txt README-REPLACEMENTS.txt

%build

%install
make install PREFIX=%{_prefix} DESTDIR=%{buildroot}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
