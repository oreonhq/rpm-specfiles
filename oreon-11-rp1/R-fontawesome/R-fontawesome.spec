%global source0_hash 1b1909d0fad5ec4c658f5c628a195b9bd93d544afa957e68e897224cfb81fb4f

Name:           R-fontawesome
Version:        %R_rpm_version 0.5.3
Release:        %autorelease
Summary:        Easily work with 'Font Awesome' Icons

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel
Requires:       fontawesome-fonts-web

%description
Easily and flexibly insert 'Font Awesome' icons into 'R Markdown' documents
and 'Shiny' apps. These icons can be inserted into HTML content through inline
'SVG' tags or 'i' tags. There is also a utility function for exporting 'Font
Awesome' icons as 'PNG' images for those situations where raster graphics are
needed.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
rm -fr %{buildroot}%{_R_libdir}/fontawesome/fontawesome
ln -s ../../../fontawesome %{buildroot}%{_R_libdir}/fontawesome
%R_save_files

%check
%R_check \--no-tests

# This and the %%ghost entry in %%files can be removed when F43 reaches EOL
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

%files -f %{R_files}
%ghost %{_R_libdir}/fontawesome/fontawesome.rpmmoved

%changelog
%autochangelog
