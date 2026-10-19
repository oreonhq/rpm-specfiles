%global source0_hash 9ea64b411f8314414f440ec765dfdf5a86c9f6159df47e2f60cff3db6b31157a
%global forgeurl https://github.com/GothenburgBitFactory/taskwarrior
Name:           task
Version:        3.5.0
Release:        1%{?dist}
Summary:        Taskwarrior - a command-line TODO list manager
License:        %{shrink:
    MIT AND
    (Apache-2.0 OR MIT) AND BSD-3-Clause AND
    (0BSD OR MIT OR Apache-2.0) AND
    Apache-2.0 AND
    Apache-2.0 AND ISC AND
    (Apache-2.0 OR BSL-1.0) AND
    (Apache-2.0 OR ISC OR MIT) AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (BSD-2-Clause OR Apache-2.0 OR MIT) AND
    BSD-3-Clause AND
    ISC AND
    ISC AND (Apache-2.0 OR ISC) AND
    ISC AND (Apache-2.0 OR ISC) AND OpenSSL AND
    MIT AND
    (MIT OR Apache-2.0) AND
    (MIT OR Zlib OR Apache-2.0) AND
    MPL-2.0 AND
    Unicode-3.0 AND
    (Unlicense OR MIT) AND
    Zlib
}
URL:            https://taskwarrior.org
Source0:        https://github.com/GothenburgBitFactory/taskwarrior/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}-%{version}-vendored.tar.xz
ExcludeArch:    %{ix86} s390x %{power64}
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  cmake
BuildRequires:  corrosion
BuildRequires:  gcc-c++
BuildRequires:  libuuid-devel
BuildRequires:  rustc
# /oreon:deps
%description
Taskwarrior is a command-line TODO list manager. It is flexible, fast,
efficient, unobtrusive, does its job then gets out of your way.

Taskwarrior scales to fit your workflow. Use it as a simple app that captures
tasks, shows you the list, and removes tasks from that list. Leverage its
capabilities though, and it becomes a sophisticated data query tool that can
help you stay organized, and get through your work.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{version} -p1 -a1
rm -f Cargo.lock
echo "Running cargo prep"
%{cargo_prep -v vendor}
echo "Checking generated cargo.toml"
cat .cargo/config.toml
echo "Checking directory contents"
ls -lash
ls -lash vendor/
find scripts/ -type f -exec chmod -x {} ';'
find scripts/ -type f -exec sed -i -e '1{\@^#!.*@d}' {} ';'
sed -i -e '1{\@^#!.*@d}' doc/rc/refresh
rm -rf ./doc/rc/refresh
rm -rf ./scripts/addons
%oreon_vendor_cargo
%build

export CARGO_HOME=%{_builddir}/%{name}-%{version}/.cargo
%cmake
%cmake_build -j1
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%cargo_vendor_manifest
%install
export CARGO_HOME=%{_builddir}/%{name}-%{version}/.cargo
%cmake_install
install -p -m 0755 -d $RPM_BUILD_ROOT/%{bash_completions_dir}/
install -D -p -m 0644 $RPM_BUILD_ROOT/%{_pkgdocdir}/scripts/bash/%{name}.sh $RPM_BUILD_ROOT%{bash_completions_dir}/%{name}
install -p -m 0755 -d $RPM_BUILD_ROOT/%{fish_completions_dir}/
install -D -p -m 0644 $RPM_BUILD_ROOT/%{_pkgdocdir}/scripts/fish/%{name}.fish $RPM_BUILD_ROOT%{fish_completions_dir}/%{name}.fish
install -p -m 0755 -d $RPM_BUILD_ROOT/%{_datadir}/%{name}
install -p -m 0644 $RPM_BUILD_ROOT/%{_pkgdocdir}/rc/* -t $RPM_BUILD_ROOT/%{_datadir}/%{name}/
rm -rfv $RPM_BUILD_ROOT/%{_pkgdocdir}/rc
rm -fv $RPM_BUILD_ROOT/%{_pkgdocdir}/INSTALL
rm -fv $RPM_BUILD_ROOT/%{_pkgdocdir}/LICENSE
rm -frv $RPM_BUILD_ROOT/%{_pkgdocdir}/scripts/{bash,fish}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
