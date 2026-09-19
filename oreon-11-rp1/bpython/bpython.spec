%global source0_hash a249306e7c4a4f16b06f98e5f6bdfc851d08221e566620aee121313c2694758d

%global srcname bpython

Name:          bpython
Summary:       Fancy curses interface to the Python interactive interpreter
Version:       0.26
Release:       3%{?dist}
URL:           http://www.bpython-interpreter.org/
License:       MIT
Source0:       https://github.com/bpython/bpython/archive/%{version}-release.tar.gz
BuildArch:     noarch
BuildRequires: desktop-file-utils
BuildRequires: make
BuildRequires: python3-devel
BuildRequires: python3-sphinx
%description
bpython is a fancy interface to the Python interpreter for Unix-like
operating systems. It has the following features:
 o in-line syntax highlighting
 o readline-like autocomplete with suggestions displayed as you type
 o expected parameter list for any Python function.
 o eewind function to pop the last line of code from memory and
   re-evaluate.
 o send the code you've entered off to a pastebin and display the
   pastebin URL for copying, etc.
 o save the code you've entered to a file
 o auto indentation

%package -n    python3-bpython
Summary:       Fancy curses interface to the Python 3 interactive interpreter
Provides:      bpython3 = %{version}-%{release}
Provides:      bpython = %{version}-%{release}
Obsoletes:     bpython < 0.17.1-6
Obsoletes:     bpython-gtk < 0.14
%{?python_provide:%python_provide python3-bpython}
Requires:      python3-curtsies >= 0.3.5
Requires:      python3-greenlet
Requires:      python3-pygments
Requires:      python3-requests > 1.2.3
Requires:      python3-six >= 1.5
Recommends:    python3dist(jedi)
Recommends:    python3dist(watchdog)
%description -n python3-bpython
bpython is a fancy interface to the Python interpreter for Unix-like
operating systems. It has the following features:
 o in-line syntax highlighting
 o readline-like autocomplete with suggestions displayed as you type
 o expected parameter list for any Python function.
 o eewind function to pop the last line of code from memory and
   re-evaluate.
 o send the code you've entered off to a pastebin and display the
   pastebin URL for copying, etc.
 o save the code you've entered to a file
 o auto indentation

This is the Python 3 build of bpython.

%package -n    python3-bpython-urwid
Summary:       Urwid interface to the Python 3 interactive interpreter
%{?python_provide:%python_provide python3-bpython-urwid}
Requires:      python3-bpython = %{version}-%{release}
Requires:      python3dist(urwid)
Requires:      python3dist(twisted)

%description -n python3-bpython-urwid
bpython is a fancy interface to the Python interpreter for Unix-like
operating systems. It has the following features:
 o in-line syntax highlighting
 o readline-like autocomplete with suggestions displayed as you type
 o expected parameter list for any Python function.
 o eewind function to pop the last line of code from memory and
   re-evaluate.
 o send the code you've entered off to a pastebin and display the
   pastebin URL for copying, etc.
 o save the code you've entered to a file
 o auto indentation

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}-release
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
pushd doc/sphinx/
make man
popd

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

# backwards compatibility links python3
ln -s bpython %{buildroot}/%{_bindir}/bpython3
ln -s bpython-curses %{buildroot}/%{_bindir}/bpython3-curses
ln -s bpdb %{buildroot}%{_bindir}/bpdb3
ln -s bpython %{buildroot}%{_bindir}/python3-bpython
install -m0644 -p -D doc/sphinx/build/man/bpython.1 \
    %{buildroot}%{_mandir}/man1/bpython.1
install -m0644 -p -D doc/sphinx/build/man/bpython-config.5 \
    %{buildroot}%{_mandir}/man5/bpython-config.5

%files -n python3-bpython
%license LICENSE
%doc AUTHORS.rst CHANGELOG.rst README.rst
%doc theme/light.theme theme/sample.theme theme/windows.theme
%{_bindir}/bpdb
%{_bindir}/bpython
%{_bindir}/bpdb3
%{_bindir}/bpython3
%{_bindir}/bpython3-curses
%{_bindir}/python3-bpython
%{python3_sitelib}/bpython/
%{python3_sitelib}/bpython-%{version}.dist-info/
%{python3_sitelib}/bpdb/
%{_mandir}/man1/bpython.1*
%{_mandir}/man5/bpython-config.5*
%{_datadir}/pixmaps/bpython.png
%{_datadir}/metainfo/org.bpython-interpreter.bpython.metainfo.xml
%{_datadir}/applications/org.bpython-interpreter.bpython.desktop

%files -n python3-bpython-urwid
%{_bindir}/bpython-urwid

%changelog
%autochangelog
