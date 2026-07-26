%global source0_hash b94ddacdfa43e9a36955ecf7d30fe9fc5a137a8209f6ab9303542a932ab61cda

%global _R_libdir_check %{nil}

Name:           R-data.table
Version:        %R_rpm_version 1.18.0
Release:        %autorelease
Summary:        Extension of `data.frame`

License:        MPL-2.0
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
Obsoletes:      %{name}-devel <= 1.18.0

%description
Fast aggregation of large data (e.g. 100GB in RAM), fast ordered joins,
fast add/modify/delete of columns by group using no copies at all, list
columns, friendly and fast character-separated-value read/write. Offers a
natural and flexible syntax, for faster development.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%ifnarch i686
%R_check
%endif

%files -f %{R_files}

%changelog
%autochangelog
