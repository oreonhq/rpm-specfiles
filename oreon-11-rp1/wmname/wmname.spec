%global source0_hash 559ad188b2913167dcbb37ecfbb7ed474a7ec4bbcb0129d8d5d08cb9208d02c5

Name:           wmname
Version:        0.1
Release:        30%{?dist}
Summary:        Prints/sets the EWMH WM name property
License:        MIT
URL:            http://tools.suckless.org/%{name}
Source0:        http://dl.suckless.org/tools/%{name}-%{version}.tar.gz
Patch0:         wmname-0.1-config.patch
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires:  make

%description
%{name} prints/sets the window manager name property of the root window similar
to how hostname(1) behaves. %{name} is a nice utility to fix problems with
JDK versions and other broken programs assuming a reparenting window manager
for instance.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .config

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}

%files
%doc LICENSE README
%{_bindir}/wmname

%changelog
%autochangelog
