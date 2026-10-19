%global source0_hash 78bd241a7e04b556ecef361ef4a1bd44835f1d6e729b74ccf58b16125323ac88
%global commit0 e9a4e7510c89613a2fe75312fba1fb8c14b3b376
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20250727
Name:           pytorch-examples
Version:        0.0^git%{date0}.%{shortcommit0}
Release:        1%{?dist}
Summary:        PyTorch Examples
License:        BSD-3-Clause AND MIT
URL:            https://github.com/pytorch/examples
Source0:        https://github.com/pytorch/examples/archive/%{commit0}/examples-%{shortcommit0}.tar.gz
Patch1:         0001-Fix-license-in-environment.py.patch
BuildArch:      noarch
ExclusiveArch:  aarch64 x86_64
Requires:  python3dist(aiohttp)
Requires:  python3dist(boto3)
Requires:  python3dist(lmdb)
Requires:  python3dist(matplotlib)
Requires:  python3dist(numpy)
Requires:  python3dist(portalocker)
Requires:  python3dist(protobuf)
Requires:  python3dist(pygame)
Requires:  python3dist(requests)
Requires:  python3dist(sentencepiece)
Requires:  python3dist(six)
Requires:  python3dist(sphinx)
Requires:  python3dist(torch)
Requires:  python3dist(torchdata)
Requires:  python3dist(torchtext)
Requires:  python3dist(torchvision)
Requires:  python3dist(tqdm)
# oreon:deps
BuildRequires:  fdupes
# /oreon:deps
%description
pytorch-examples showcases examples of using PyTorch.  The goal
is to have curated, short, few/no dependencies high quality examples
that are substantially different from each other that can be
emulated in your existing work.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n examples-%{commit0}
# *** WARNING: .../distributed/ddp/run_example.sh is executable but has no shebang, removing executable bit
sed -i -e 's@# /bin/bash@#!/usr/bin/bash@' distributed/ddp/run_example.sh
# mangling shebang in .../distributed/minGPT-ddp/run_example.sh from /bin/bash to #!/usr/bin/bash
sed -i -e 's@#!/bin/bash@#!/usr/bin/bash@' distributed/minGPT-ddp/run_example.sh
# *** WARNING: .../distributed/tensor_parallelism/tensor_parallel_example.py is executable but has no shebang, removing executable bit
# Leave as-is
# *** ERROR: ambiguous python shebang in .../regression/main.py: #!/usr/bin/env python. Change it to python3 (or python2) explicitly.
sed -i -e 's@usr/bin/env python@usr/bin/python3@' regression/main.py

# Remove some cruft rpmlint found
# pytorch-examples.noarch: E: zero-length /usr/share/pytorch-examples/docs/source/_static/.gitkeep
find . -name .gitkeep -type f -delete
# pytorch-examples.noarch: E: version-control-internal-file /usr/share/pytorch-examples/.gitignore
find . -name .gitignore -type f -delete
# pytorch-examples.noarch: W: hidden-file-or-dir /usr/share/pytorch-examples/.github
rm -rf .github
# pytorch-examples.noarch: W: hidden-file-or-dir /usr/share/pytorch-examples/cpp/.clang-format
find . -name .clang-format -type f -delete

# Fix some premissions
for f in `find . -name '*.sh'`; do
    chmod 755 $f
    sed -i -e 's@/usr/bin/env bash@/usr/bin/bash@' $f
done
for f in `find . -name '*.py'`; do
    sed -i -e 's@/usr/bin/env python3@/usr/bin/python3@' $f
done
chmod 755 docs/source/conf.py

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -p -r . %{buildroot}%{_datadir}/%{name}
rm %{buildroot}%{_datadir}/%{name}/README.md
rm %{buildroot}%{_datadir}/%{name}/LICENSE
%fdupes %{buildroot}%{_datadir}/%{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
