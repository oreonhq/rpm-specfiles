%global source0_hash 41534ded3c4f6153e53742ce171d27527155d79a58656d1047154f713f93f113

Name:		winpdb
Version:	2.0.0.1
Release:	6%{?dist}
Summary:	An advanced python debugger
License:	GPL-2.0-or-later
URL:		https://pypi.org/project/winpdb-reborn
Source0:	https://files.pythonhosted.org/packages/d9/8f/c8033e1a075d8205a2f950a40644d363f63b11698655f620b5f4d6e7ace0/winpdb-reborn-2.0.0.1.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		https://github.com/bluebird75/winpdb/commit/d1a4430ac8da69d3a1cd4a848c9135f093b90123.patch
Patch1:		https://github.com/bluebird75/winpdb/commit/5c2f5232b95715c5e8efbd155dd38c262f5e79d0.patch
Patch2:		https://github.com/bluebird75/winpdb/commit/215712d75cf89b0678d563237746be647d5f25e7.patch
Patch3:		https://github.com/bluebird75/winpdb/commit/613e4532d93b728bef7b2c8e529a431bbe6ecc19.patch
Patch4:		https://github.com/bluebird75/winpdb/commit/2a3ca49275ee8461009dbe5a4aefef4b57dec729.patch
Patch5:		https://github.com/bluebird75/winpdb/commit/ed617311de97300c1ce9de9ee6931dc7141cfd93.patch
Patch6:		winpdb-2.0.0.1-no-imp.patch
BuildArch:	noarch
BuildRequires: 	python3-devel, desktop-file-utils
BuildRequires: 	python3-setuptools, dos2unix
Requires:	python3-crypto, python3-wxpython4
Provides:	winpdb-reborn = %{version}-%{release}

%description
Winpdb is an advanced python debugger, with support for smart breakpoints, 
multiple threads, namespace modification, embedded debugging, encrypted 
communication and speed of up to 20 times that of pdb.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-reborn-%{version}
for i in *.py rpdb/*.py; do
	dos2unix $i
done
%patch -P0 -p1 -b .typofix
%patch -P1 -p1 -b .deprecated-function
%patch -P2 -p1 -b .undefined
%patch -P3 -p1 -b .small-typo
%patch -P4 -p1 -b .no-print-if-no-file
%patch -P5 -p1 -b .use-public-stderr
%patch -P6 -p1 -b .no-imp
sed -i 's|/usr/bin/env python|/usr/bin/python3|g' rpdb2.py
sed -i 's|/usr/bin/env python|/usr/bin/python3|g' winpdb.py

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --skip-build --root=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -m0644 -p %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications

desktop-file-install 		\
	--dir $RPM_BUILD_ROOT%{_datadir}/applications	\
	%{SOURCE1}

chmod +x $RPM_BUILD_ROOT%{python3_sitelib}/rpdb2.py $RPM_BUILD_ROOT%{python3_sitelib}/winpdb.py

%files
%doc README.md
%{_bindir}/*
%{python3_sitelib}/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
%autochangelog
