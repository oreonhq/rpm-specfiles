%global source0_hash 907d99c0196539a98d76eb84226c9fb25580de382e4e80e842c9305508b3aaa9
%global py3_shebang_flags %(echo %py3_shebang_flags | sed s/s//)
%global gap_pkgname jupyterkernel
%global gap_upname  JupyterKernel
%global giturl      https://github.com/gap-packages/JupyterKernel
Name:           gap-pkg-%{gap_pkgname}
Version:        1.5.1
Release:        1%{?dist}
Summary:        Jupyter kernel written in GAP
License:        BSD-3-Clause
URL:            https://gap-packages.github.io/JupyterKernel/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): demos gap tst
BuildOption(check): tst/testall.g
Requires:       gap-pkg-crypting
Requires:       gap-pkg-io
Requires:       gap-pkg-json
Requires:       gap-pkg-uuid
Requires:       gap-pkg-zeromqinterface
Requires:       python-jupyter-filesystem
# oreon:deps
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-crypting
BuildRequires:  gap-pkg-io
BuildRequires:  gap-pkg-json
BuildRequires:  gap-pkg-uuid
BuildRequires:  gap-pkg-zeromqinterface
BuildRequires:  python3dist(jupyter-client)
BuildRequires:  python3dist(notebook)
# /oreon:deps
%description
This package implements the Jupyter protocol in GAP.

%package doc
License:        BSD-3-Clause AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Jupyter kernel for GAP documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gap_upname}-%{version}

%install -a
mkdir -p %{buildroot}%{_bindir}
cp -p bin/jupyter-kernel-gap %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/jupyter/kernels
cp -a etc/jupyter %{buildroot}%{_datadir}/jupyter/kernels/gap-4
mkdir -p %{buildroot}%{_datadir}/jupyter/nbextensions
cp -a etc/gap-mode %{buildroot}%{_datadir}/jupyter/nbextensions
mkdir -p %{buildroot}%{_sysconfdir}/jupyter/nbconfig/notebook.d
cp -p etc/gap-mode.json %{buildroot}%{_sysconfdir}/jupyter/nbconfig/notebook.d
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gap-pkg-jupyterkernel-doc -f %{oreon_filedir}/gap-pkg-jupyterkernel-doc.list

%changelog

%autochangelog
