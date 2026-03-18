# perl-B-COW

`B::COW` provides some naïve additional B helpers to check the Copy On Write
(COW) status of one SvPV (a Perl string variable).

A COWed SvPV is sharing its string (the PV) with other SvPVs. It's a (kind of)
Read Only C string, which would be Copied On Write (COW). More than one SV can
share the same PV, but when one PV needs to alter it, it would perform a copy
of it, decreasing the `COWREFCNT` counter. One SV can then drop the COW flag when
it's the only one holding a pointer to the PV. The `COWREFCNT` is stored at the
end of the PV, after the null byte terminating the string. That value is
limited to 255: when we reach 255, a new PV would be created.
