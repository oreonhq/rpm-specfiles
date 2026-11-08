# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 51cc11666391ab6f092070437ac747002ff46f3e4113a3622177ee6b488bfc53
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: python3-build
Version: 1.6.1
Release: 1%{?dist}
Summary: Simple, correct Python build frontend
License: MIT
URL: https://pypi.org/project/build/
Source0: https://files.pythonhosted.org/packages/source/b/build/build-%{version}.tar.gz
BuildArch: noarch
Requires: python3
Requires: python3-packaging
Requires: python3-pyproject-hooks
Provides: python3dist(build) = %{version}

BuildRequires: oreon-rpm-macros
BuildRequires: python3

%description
build is a PEP 517 build frontend for Python packages.

%prep
%oreon_sha256
%autosetup -n build-%{version} -p1

%build


%install
sitelib=$(python3 -c 'import sysconfig; print(sysconfig.get_path("purelib"))')
mkdir -p %{buildroot}$sitelib
cp -a src/build %{buildroot}$sitelib/
python3 - %{buildroot} $sitelib build %{version} <<'EOF'
import configparser, glob, os, shutil, sys, tomllib
root, site, dist, ver = sys.argv[1:]
d = os.path.join(root + site, dist + "-" + ver + ".dist-info")
os.makedirs(d)
shutil.copy("PKG-INFO", os.path.join(d, "METADATA"))
open(os.path.join(d, "INSTALLER"), "w").write("rpm\n")
eps = {}
egg = glob.glob("*.egg-info/entry_points.txt") + glob.glob("src/*.egg-info/entry_points.txt")
if egg:
    cp = configparser.ConfigParser(delimiters=("=",), interpolation=None)
    cp.optionxform = str
    cp.read(egg[0])
    eps = {s: {k: v.strip() for k, v in cp[s].items()} for s in cp.sections()}
else:
    proj = tomllib.load(open("pyproject.toml", "rb")).get("project", {})
    if proj.get("scripts"):
        eps["console_scripts"] = proj["scripts"]
    eps.update(proj.get("entry-points", {}))
if eps:
    with open(os.path.join(d, "entry_points.txt"), "w") as f:
        for g, v in eps.items():
            f.write("[" + g + "]\n" + "".join(k + " = " + x + "\n" for k, x in v.items()) + "\n")
for k, x in eps.get("console_scripts", {}).items():
    mod, _, fn = x.partition(":")
    b = root + "/usr/bin/" + k
    os.makedirs(os.path.dirname(b), exist_ok=True)
    open(b, "w").write("#!/usr/bin/python3\nimport sys\nfrom " + mod + " import " + fn.split(".")[0] + "\nsys.exit(" + fn + "())\n")
    os.chmod(b, 0o755)
EOF
find %{buildroot} -type f -exec grep -I -l -E '^#! */usr/bin/env python' {} + | while read -r f; do
  sed -i '1s|^#! */usr/bin/env python.*|#!/usr/bin/python3|' "$f"
done
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_infodir}/dir
%oreon_filelist
while read -r f; do
  case "$f" in
    *.py) printf '%s\n' "$(dirname "$f")/__pycache__/*" ;;
  esac
done < %{_builddir}/%{name}.files | sort -u >> %{_builddir}/%{name}.files

%files -f %{_builddir}/%{name}.files
%license LICENSE
