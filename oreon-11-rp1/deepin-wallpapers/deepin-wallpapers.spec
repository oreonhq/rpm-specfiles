%global source0_hash none

Name:           deepin-wallpapers
Version:        1.7.16
Release:        %autorelease
Summary:        Deepin Wallpapers provides wallpapers of DDE
License:        CC-BY-4.0
URL:            https://github.com/linuxdeepin/deepin-wallpapers
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  make

Requires(post): %{_sbindir}/alternatives
Requires(postun): %{_sbindir}/alternatives

%description
%{summary}.

%prep
%autosetup -p1 -n %{name}-%{version}

%build

%install
install -d %{buildroot}%{_datadir}/wallpapers/deepin/
cp deepin/* %{buildroot}%{_datadir}/wallpapers/deepin/

install -d %{buildroot}%{_datadir}/backgrounds/deepin/
touch %{buildroot}%{_datadir}/backgrounds/default_background.jpg

%post
if [ $1 -ge 1 ]; then
  %{_sbindir}/alternatives --install %{_datadir}/backgrounds/default_background.jpg \
    deepin-default-background %{_datadir}/wallpapers/deepin/desktop.jpg 50
fi

%postun
if [ $1 -eq 0 ]; then
  %{_sbindir}/alternatives --remove deepin-default-background %{_datadir}/wallpapers/deepin/desktop.jpg
fi

%files
%doc README.md
%license LICENSE
%ghost %{_datadir}/backgrounds/default_background.jpg
%{_datadir}/backgrounds/deepin/
%dir %{_datadir}/wallpapers
%{_datadir}/wallpapers/deepin/

%changelog
%autochangelog
