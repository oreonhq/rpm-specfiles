# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 3ff8b3b5492a0aa66960f4419365a86b84e013070d4313e4d4a6894f5d64d6bc
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: python3-setuptools
Version: 84.2.1
Release: 2%{?dist}
Summary: Easily build and distribute Python packages
License: MIT
URL: https://pypi.org/project/setuptools/
Source0: https://files.pythonhosted.org/packages/source/s/setuptools/setuptools-%{version}.tar.gz
BuildArch: noarch
Requires: python3
Provides: python3dist(setuptools) = %{version}

BuildRequires: oreon-rpm-macros
BuildRequires: python3

%description
Setuptools is the build backend and packaging library used by most Python
projects.

%prep
%oreon_sha256
%autosetup -n setuptools-%{version} -p1

%build


%install
sitelib=$(python3 -c 'import sysconfig; print(sysconfig.get_path("purelib"))')
mkdir -p %{buildroot}$sitelib
cp -a setuptools _distutils_hack %{buildroot}$sitelib/
python3 - %{buildroot} $sitelib setuptools %{version} <<'EOF'
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
cat > %{buildroot}$sitelib/distutils-precedence.pth <<'EOF'
import os; var = 'SETUPTOOLS_USE_DISTUTILS'; enabled = os.environ.get(var, 'local') == 'local'; enabled and __import__('_distutils_hack').add_shim(); 
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

mkdir -p %{buildroot}%{python_wheel_dir}
python3 - %{buildroot} $sitelib %{version} <<'EOF'
import base64, hashlib, os, sys, zipfile
root, site, ver = sys.argv[1:]
base = os.path.join(root + site, "setuptools")
wheel = os.path.join(root, "usr/share/python-wheels", "setuptools-" + ver + "-py3-none-any.whl")
os.makedirs(os.path.dirname(wheel), exist_ok=True)
names = []
for dirpath, dirnames, filenames in os.walk(base):
    dirnames[:] = [x for x in dirnames if x != "__pycache__"]
    for name in filenames:
        p = os.path.join(dirpath, name)
        rel = os.path.relpath(p, root + site)
        if rel.endswith(".pyc"):
            continue
        names.append((p, rel))
pth = os.path.join(root + site, "distutils-precedence.pth")
names.append((pth, "distutils-precedence.pth"))
d = os.path.join(root + site, "setuptools-" + ver + ".dist-info")
for name in os.listdir(d):
    if name == "INSTALLER":
        continue
    names.append((os.path.join(d, name), "setuptools-" + ver + ".dist-info/" + name))
with zipfile.ZipFile(wheel, "w", zipfile.ZIP_DEFLATED) as z:
    record = []
    for p, rel in sorted(names, key=lambda x: x[1]):
        data = open(p, "rb").read()
        z.writestr(rel, data)
        digest = base64.urlsafe_b64encode(hashlib.sha256(data).digest()).rstrip(b"=").decode()
        record.append("%s,sha256=%s,%d" % (rel, digest, len(data)))
    record.append("setuptools-%s.dist-info/RECORD,," % ver)
    z.writestr("setuptools-%s.dist-info/WHEEL" % ver,
               "Wheel-Version: 1.0\nGenerator: oreon-rpm-macros\nRoot-Is-Purelib: true\nTag: py3-none-any\n")
    z.writestr("setuptools-%s.dist-info/RECORD" % ver, "\n".join(record) + "\n")
EOF

%files -f %{_builddir}/%{name}.files
%license LICENSE

%package -n python-setuptools-wheel
Summary: The setuptools wheel
Provides: python-setuptools-wheel = %{version}

%description -n python-setuptools-wheel
A Python wheel of setuptools to use with venv.

%files -n python-setuptools-wheel
%dir %{python_wheel_dir}/
%{python_wheel_dir}/setuptools-%{version}-py3-none-any.whl
