%global source0_hash ff6124151dd13ebd014468c3eb974de7078b7b642b2805b002bcacae4016b267
%bcond check 0
%bcond_without cli
%bcond_without gui
Summary:        File Access Policy Analyzer
Name:          fapolicy-analyzer
Version:       1.5.1
Release:        1%{?dist}
SourceLicense: GPL-3.0-or-later
License:       %{shrink:
    GPL-3.0-or-later AND
    Apache-2.0 AND
    CC0-1.0 AND
    ISC AND
    MIT AND
    MPL-2.0 AND
    Unicode-DFS-2016 AND
    (0BSD OR MIT OR Apache-2.0) AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (MIT OR X11 OR Apache-2.0) AND
    (MIT OR Zlib OR Apache-2.0) AND
    (Unlicense OR MIT)
    }
URL:           https://github.com/ctc-oss/fapolicy-analyzer
Source0:        https://github.com/ctc-oss/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:       %{url}/releases/download/v%{version}/vendor-docs-%{version}.tar.gz
ExcludeArch:   %{ix86}
Requires:      %{name}-cli
Requires:      %{name}-gui
# oreon:deps
BuildRequires:  audit-libs-devel
BuildRequires:  babel
BuildRequires:  cargo-rpm-macros
BuildRequires:  clang
BuildRequires:  dbus-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  golang
BuildRequires:  itstool
BuildRequires:  lmdb-devel
BuildRequires:  maturin
BuildRequires:  python3-devel
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  uv
# /oreon:deps
%description
Tools to assist with the configuration and management of fapolicyd.

%package cli
Summary:       File Access Policy Analyzer CLI
%description cli
CLI Tools to assist with the configuration and management of fapolicyd.

%package gui
Summary:       File Access Policy Analyzer GUI
Requires:      python3
Requires:      python3-gobject
Requires:      python3-configargparse
Requires:      python3-more-itertools
Requires:      python3-importlib-metadata
Requires:      python3-tomli
Requires:      python3-matplotlib-gtk3
%global __requires_exclude ^python3\.[0-9]+dist\\(rx\\)
Requires:      python3-rx
Requires:      gtk3
Requires:      gtksourceview3
Requires:      gnome-icon-theme
Requires:      mesa-dri-drivers
Requires:      webkit2gtk4.1
%global module          fapolicy_analyzer
%global module_version  %{lua: v = string.gsub(rpm.expand("%{?version}"), "~dev", ".dev"); \
                               v = string.gsub(v, "~rc",  "rc"); print(v) }
%description gui
GUI Tools to assist with the configuration and management of fapolicyd.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}

%if %{without cli}
# disable tools crate
sed -i '/tools/d' Cargo.toml
%endif

%if %{without gui}
# disable pyo3 crate
sed -i '/pyo3/d' Cargo.toml
%endif

# extract our doc sourcs
tar xvzf %{SOURCE1}

# patch pyproject.toml version
scripts/version.py --patch --toml pyproject.toml --version %{module_version}

# capture build info
scripts/build-info.py --os --time

# enable the audit feature for 39 and up

%build

export RUSTFLAGS="%{build_rustflags}"
%if %{with cli}
cargo build --release -p fapolicy-tools --bin tdb
cargo build --release -p fapolicy-tools --bin faprofiler
cargo build --release -p fapolicy-tools --bin rulec --features pretty
%endif
%if %{with gui}
pybabel compile -f -d locale -D fapolicy-analyzer
%{python3} help build
maturin build --release --skip-auditwheel -o dist
%endif
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%if %{with cli}
install -D target/release/tdb %{buildroot}/%{_sbindir}/%{name}-cli-trust
install -D target/release/faprofiler %{buildroot}/%{_sbindir}/%{name}-cli-profiler
install -D target/release/rulec %{buildroot}/%{_sbindir}/%{name}-cli-rules
%endif
%if %{with gui}
wheel=$(basename dist/*.whl)
%{py3_install_wheel $wheel}
%{python3} help install --dest %{buildroot}/%{_datadir}/help
install -D bin/%{name} %{buildroot}/%{_sbindir}/%{name}
install -D data/%{name}.8 -t %{buildroot}/%{_mandir}/man8/
install -D data/%{name}-cli-*.8 -t %{buildroot}/%{_mandir}/man8/
install -D data/config.toml -t %{buildroot}%{_sysconfdir}/%{name}/
desktop-file-install data/%{name}.desktop
find locale -name %{name}.mo -exec cp --parents -rv {} %{buildroot}/%{_datadir} \;
%find_lang %{name} --with-gnome
rm %{buildroot}/%{_bindir}/gui
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%check

%if %{with gui}
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%endif
%files -f %{oreon_filedir}/main.list
%files -n fapolicy-analyzer-cli -f %{oreon_filedir}/fapolicy-analyzer-cli.list
%files -n fapolicy-analyzer-gui -f %{oreon_filedir}/fapolicy-analyzer-gui.list

%changelog

%autochangelog
