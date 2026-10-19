%global source0_hash 1b1909d0fad5ec4c658f5c628a195b9bd93d544afa957e68e897224cfb81fb4f
Name:           R-fontawesome
Version:        %R_rpm_version 0.5.3
Release:        1%{?dist}
Summary:        Easily work with 'Font Awesome' Icons
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=fontawesome&version=%{version}#/fontawesome_%{version}.tar.gz
BuildArch:      noarch
Requires:       fontawesome-fonts-web
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Easily and flexibly insert 'Font Awesome' icons into 'R Markdown' documents
and 'Shiny' apps. These icons can be inserted into HTML content through inline
'SVG' tags or 'i' tags. There is also a utility function for exporting 'Font
Awesome' icons as 'PNG' images for those situations where raster graphics are
needed.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
%R_install
rm -fr %{buildroot}%{_R_libdir}/fontawesome/fontawesome
ln -s ../../../fontawesome %{buildroot}%{_R_libdir}/fontawesome
%R_save_files
%oreon_autofiles main

%check

%R_check \--no-tests
%pretrans -p <lua>

path = "%{_R_libdir}/fontawesome/fontawesome"
st = posix.stat(path)
if st and st.type == "directory" then
  status = os.rename(path, path .. ".rpmmoved")
  if not status then
    suffix = 0
    while not status do
      suffix = suffix + 1
      status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
    end
    os.rename(path, path .. ".rpmmoved")
  end
end
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
