%global source0_hash 2f02f94cb4640fa00bb9c69b2d4781d24e2b217f8efda5b679b4b6ad93e3214b

Name:           python-goocalendar
Version:        0.8.0
Release:        %autorelease
Summary:        A calendar widget for GTK using PyGoocanvas

License:        GPL-2.0-or-later
URL:            https://code.tryton.org/goocalendar
Source:         %{pypi_source GooCalendar}

BuildArch:      noarch
BuildRequires:  python3-devel
# Documentation
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-book-theme)
BuildRequires:  python3dist(sphinx-copybutton)
BuildRequires:  texinfo
# Import check
BuildRequires:  gobject-introspection-devel
BuildRequires:  goocanvas2-devel
BuildRequires:  gtk3-devel
BuildRequires:  python3-gobject
BuildRequires:  python3-gobject-devel

%global _description %{expand:
A calendar widget for GTK using PyGooCanvas.

Example usage::

    >>> import datetime
    >>> import goocalendar
    >>> event_store = goocalendar.EventStore()
    >>> calendar = goocalendar.Calendar(event_store)
    >>> event = goocalendar.Event('Birthday',
    ...     datetime.date.today(),
    ...     bg_color='lightgreen')
    >>> event_store.add(event)}

%description %_description

%package -n     python3-goocalendar
Summary:        %{summary}

%description -n python3-goocalendar %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n GooCalendar-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
pushd doc
sphinx-build -b texinfo . texinfo
pushd texinfo
makeinfo --docbook GooCalendar.texi
popd
popd

%install
%pyproject_install
%pyproject_save_files -l goocalendar
mkdir -p %{buildroot}%{_datadir}/help/en/python-goocalendar
install -m644 doc/texinfo/GooCalendar.xml %{buildroot}%{_datadir}/help/en/python-goocalendar

%check
%pyproject_check_import

%files -n python3-goocalendar -f %{pyproject_files}
%doc README
%dir  %{_datadir}/help/en
%lang(en) %{_datadir}/help/en/python-goocalendar

%changelog
%autochangelog
