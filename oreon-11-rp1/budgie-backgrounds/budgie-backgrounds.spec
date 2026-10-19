%global source2_hash 3430854f668d5e05950406f06fb3d73075c55fb8e2757868786afa0fa324b2b7
%global source0_hash c760da9869f3ef7524ffc19936c99bbb54f728ec4b798caecac470a981711e41
Name:           budgie-backgrounds
Version:        4.1
Release:        1%{?dist}
Summary:        Default set of background images for the Budgie Desktop
License:        CC0-1.0
URL:            https://github.com/BuddiesOfBudgie/budgie-backgrounds
Source0:        https://github.com/BuddiesOfBudgie/%{name}/releases/download/v%{version}/%{name}-v%{version}.tar.xz
Source1:        %{url}/releases/download/v%{version}/%{name}-v%{version}.tar.xz.asc
Source2:        https://serebit.com/openpgp/git-at-serebit-dot-com.asc
BuildArch:      noarch
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  jhead
BuildRequires:  meson
# /oreon:deps
%description
Default set of background images for the Budgie Desktop.

%prep

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
