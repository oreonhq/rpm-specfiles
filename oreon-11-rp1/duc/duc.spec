%global source0_hash e91592e367f3f8be671899660756b25e2c37f316c42ebd2a36dd684be3e2f25a
%if %{undefined el8}
%bcond_without opengl
%else
%ifarch x86_64
%bcond_without opengl
%else
%bcond_with opengl
%endif
%endif
Name:           duc
Version:        1.4.6
Release:        1%{?dist}
Summary:        Disk usage tools
License:        LGPL-3.0-or-later AND MIT-Khronos-old
URL:            https://duc.zevv.nl/
Source0:        https://github.com/zevv/duc/releases/download/%{version}/duc-%{version}.tar.gz
Source1:        duc.desktop
%if %{with opengl}
%endif
# oreon:deps
BuildRequires:  cairo-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  glfw-devel
BuildRequires:  libglvnd-devel
BuildRequires:  ncurses-devel
BuildRequires:  pango-devel
BuildRequires:  pcre2-devel
BuildRequires:  tokyocabinet-devel
BuildRequires:  uthash-devel
# /oreon:deps
%description
Duc is a collection of tools for indexing, inspecting and visualizing
disk usage. Duc maintains a database of accumulated sizes of directories
of the file system, and allows you to query this database with some tools,
or create fancy graphs showing you where your bytes are.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

(
cd src/libduc
for i in ut*.h; do
    ln -sf %{_includedir}/$i $i
done
)

%build

%configure %{?with_opengl:--enable-opengl --disable-x11} \
           %{!?with_opengl:--disable-opengl --enable-x11}
%make_build
%install
%make_install
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
%oreon_autofiles main

%check

%{buildroot}%{_bindir}/duc help
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
