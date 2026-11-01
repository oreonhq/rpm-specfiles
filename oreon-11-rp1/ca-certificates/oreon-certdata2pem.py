#!/usr/bin/python3
# SPDX-License-Identifier: MIT
# Convert Mozilla certdata.txt into a PEM bundle of roots trusted for
# TLS server authentication. Part of Oreon's ca-certificates package.
import base64
import sys
import textwrap


def parse(path):
    objs, cur, lines = [], None, iter(open(path, encoding="utf-8"))
    for line in lines:
        line = line.rstrip("\n")
        if not line or line.startswith("#"):
            if cur is not None and not line:
                objs.append(cur)
                cur = None
            continue
        if line.startswith("BEGINDATA"):
            continue
        parts = line.split(" ", 2)
        if parts[0] == "CKA_CLASS":
            if cur is not None:
                objs.append(cur)
            cur = {}
        if cur is None:
            continue
        if len(parts) > 1 and parts[1] == "MULTILINE_OCTAL":
            data = bytearray()
            for l in lines:
                l = l.strip()
                if l == "END":
                    break
                for oc in l.split("\\")[1:]:
                    data.append(int(oc, 8))
            cur[parts[0]] = bytes(data)
        else:
            cur[parts[0]] = parts[2] if len(parts) > 2 else ""
    if cur is not None:
        objs.append(cur)
    return objs


def main(src, dst):
    objs = parse(src)
    trusted = set()
    for o in objs:
        if o.get("CKA_CLASS") == "CKO_NSS_TRUST" and \
           o.get("CKA_TRUST_SERVER_AUTH") == "CKT_NSS_TRUSTED_DELEGATOR":
            trusted.add((o.get("CKA_ISSUER"), o.get("CKA_SERIAL_NUMBER")))
    count = 0
    with open(dst, "w", encoding="utf-8") as out:
        for o in objs:
            if o.get("CKA_CLASS") != "CKO_CERTIFICATE":
                continue
            if (o.get("CKA_ISSUER"), o.get("CKA_SERIAL_NUMBER")) not in trusted:
                continue
            label = o.get("CKA_LABEL", "").strip('"')
            b64 = base64.b64encode(o["CKA_VALUE"]).decode()
            out.write("# %s\n-----BEGIN CERTIFICATE-----\n%s\n-----END CERTIFICATE-----\n"
                      % (label, "\n".join(textwrap.wrap(b64, 64))))
            count += 1
    if count < 100:
        sys.exit("only %d trusted roots found, refusing to write a short bundle" % count)
    print("wrote %d certificates" % count)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
