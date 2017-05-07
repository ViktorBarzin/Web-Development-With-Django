import sys
from celery.result import AsyncResult
from tasks import add, pdf_site


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise Exception('Call with 3 arguments!')

    if sys.argv[1].lower() == 'download':
        site = sys.argv[2].lower()
        result = pdf_site.delay(site, 'downloads/{}.pdf'.format(site.replace('.','_')))
        print('PDF for {} will be generated. Check with this UUID:{}'.format(site, result.task_id))

    elif sys.argv[1].lower() == 'check':
        task_id = sys.argv[2].lower()
        res = AsyncResult(task_id)
        if res.ready():
            print('PDF for {} is located in download/{}.pdf'.format(res.result, res.result.replace('.','_')))
        else:
            print('Still not ready')

